from typing import Dict, List
from websockets.sync.client import connect, ClientConnection
import requests
import threading
from urllib.parse import quote
import notebookforms.items as items
import json
import time

class Form:
    ws: ClientConnection
    def __init__(self, ws: ClientConnection):
        self.ws = ws
        
    def close(self):
        self.ws.send(json.dumps({
            "type": "session_close",
            "data": None
        }))
    
    def send_canvas(self, canvas:items.FormCanvas) -> Dict[str, str]:
        print(canvas.get_items())
        self.ws.send(json.dumps({
            "type": "session_canvas",
            "data": canvas.get_items()
        }))
        
        resp = self.ws.recv()
        msg = json.loads(resp)
        
        if msg["type"] == "session_submit":
            return msg["data"]
        else:
            print("Unexpected message:", msg)
            return {}
        
    def input(self, question: str, valueType:str = 'text', placeholder: str = None):
        c = items.FormCanvas()
        c += items.QuestionItem(question)
        c += items.InputItem("input", placeholder, valueType)
        c += items.SubmitButtonItem()
        
        return self.send_canvas(c)["input"]
    
    def ab_buttons(self, question: str, buttons: List[List[str]] = None):
        c = items.FormCanvas()
        c += items.QuestionItem(question)
        c += items.ABButtonsItem("ab_buttons", buttons)
        
        return self.send_canvas(c)["ab_buttons"]
    
    def select(self, question: str, multiple:bool = None, options: List[List[str]] = None, autoSubmit: bool = None)->List[str]:
        c = items.FormCanvas()
        c += items.QuestionItem(question)
        c += items.SelectItem("select", multiple, options, autoSubmit)
        if autoSubmit != True:
            c += items.SubmitButtonItem()
        
        return self.send_canvas(c)["select"]

class FormHandler:
    
    __api_endpoint = "http://localhost:8001/api"
    __ws_endpoint = "ws://localhost:8001/api"
    
    def __init__(self, func: callable, token:str, schema: Dict[str, str]):
        self.func = func
        self.token = token
        self.schema = schema
        
        self.__register_schema()
    
    def serve(self):
        self.__listen_for_sesions()
    
    def __listen_for_sesions(self):
        with connect(f"{self.__ws_endpoint}/listen?token={quote(self.token)}") as websocket:
            while True:
                try:
                    msg = json.loads(websocket.recv())
                    if msg["type"] == "new_session":
                        print("New session:", msg["data"])
                        threading.Thread(target=self.__run_session, args=(msg["data"],)).start()
                    else:
                        print("Unexpected message:", msg)
                except Exception:
                    print("Connection closed.")
                    break
                
    def __run_session(self, session_id: str):
        start = time.process_time_ns()
        with connect(f"{self.__ws_endpoint}/session?token={quote(self.token)}&session={quote(session_id)}") as websocket:
            print("Connected.")
            form = Form(websocket)
            self.func(form)
            form.close()
        end = time.process_time_ns()
        print("Session done in", end)
                    
    def __register_schema(self):
        return
        # TODO: reactivate
        requests.post(f"{self.__api_endpoint}/update_schema", params={
            "token": self.token
        }, json=self.schema)
    
def form(*, token:str = None, schema:Dict[str, str] = None) -> FormHandler:
    def wrapper(func):
        return FormHandler(func, token, schema)
    return wrapper
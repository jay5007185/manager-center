# %%
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from . import login_page as login_page
from . import http_exception_403, http_exception_404
from datetime import datetime


# %%
server_port = 8089

app = FastAPI()


# %%
@app.middleware("http")
async def verify_access(request: Request, call_next):
    try:
        response = await call_next(request)
        
        # cookie_keys = list(request.cookies.keys())
        # print("######## cookie")
        # for i in cookie_keys:
        #     print('##', request.cookies[i])
        
        # print("######## url", request.url)
        # print("######## headers", request.headers.keys())
        # for i in request.headers.keys():
        #     print("##",i,"##",request.headers.get(i))

        # print("######## client", request.client) 

        if request.url.path in [
            "/login_page/", 
            "/logging_login/", 
            "/player_profiler/", 
            "/withdraw_check/", 
            "/withdraw_check_history/",
            "/lottery_watcher_by_product/", 
            "/lottery_watcher_by_member/", 
            "/plus_lottery_watcher_by_member/", 
            "/member_bet_product_info/",
            "/plus_lottery_watcher_by_member_multi_product/",
            "/lottery_report_by_product/",
            "/login_history_query/",
        ]:
    
            
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Page Not Found")
        
        return response
    
    except HTTPException as exc:
        if exc.status_code == 403:
            return RedirectResponse("/403-Forbidden/")
        elif exc.status_code == 404:
            return RedirectResponse("/404-NotFound/")
    

@app.get("/")
def landing_page():
    return RedirectResponse("/login_page")

@app.get("/status")
def get_status():
    content = {  
        "code":200,
        "status":"success",
        "data": [{"message": "This is a 200 OK response."}],
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return JSONResponse(content=content, status_code=200)

app.mount("/login_page/", WSGIMiddleware(login_page.app.server))
app.mount("/403-Forbidden/", WSGIMiddleware(http_exception_403.app.server))
app.mount("/404-NotFound/", WSGIMiddleware(http_exception_404.app.server))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("dash_server:app", host='0.0.0.0', port=server_port, reload=True)


# %%

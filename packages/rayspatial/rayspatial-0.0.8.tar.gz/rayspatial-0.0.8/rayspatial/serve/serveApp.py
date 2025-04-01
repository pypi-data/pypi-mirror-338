from starlette.requests import Request
from ray import serve
import ray

@serve.deployment(num_replicas=10, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
class ServeApp:
    async def __call__(self, request: Request):
        # 需要在rayspatial包的根目录下创建__init__.py文件
        # 在__init__.py中定义__version__变量
        import rayspatial
        print(f"rayspatial version: {rayspatial.__version__}")
        requestJson = await request.json()
        params = requestJson["params"]
        header = requestJson["header"]
        return rayspatial.serve.exe.ServeExecute.execute_serve(params, header)
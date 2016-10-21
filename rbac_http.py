import json
from trellio import Host, HTTPService, TCPService, get, post, api, publish, Request, Response, put, delete
from serializers import RoleSerializer

class UserRoleService(HTTPService):
    role_helper = RoleHelper()
    def __init__(self, ip, port):
        super(UserRoleService, self).__init__("UserRoleService", 1, ip, port)

    @get(path='/resource/access/')
    def check_access(self, request: Request):
        user_id = request.GET.get('user_id')
        roles = self.role_helper.get_roles(user_id)
        return Response(data=RoleSerializer(roles).data)

    @post(path='/role/')
    def create_role(self, request: Request):
        data = yield from request.json()
        return Response(status=200, body=(json.dumps(data)).encode())


    @put(path='/role/')
    def create_role(self, request: Request):
        data = yield from request.json()
        return Response(status=200, body=(json.dumps(data)).encode())


    @delete(path='/role/')
    def create_role(self, request: Request):
        data = yield from request.json()
        return Response(status=200, body=(json.dumps(data)).encode())



if __name__ == '__main__':
    REGISTRY_PORT = 4500
    REDIS_PORT = 6379
    ROLE_HOST = '127.0.0.1'
    ROLE_HTTP_PORT = 4501
    http = UserRoleService(ROLE_HOST, ROLE_HTTP_PORT)
    Host.configure('UserRoleService')
    Host.attach_http_service(http)
    Host.run()
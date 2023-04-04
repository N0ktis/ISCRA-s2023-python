import logging
import os.path
import socket
import enum
import threading
import asyncio

class Status(enum.Enum):
    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]

    OK = (200, 'OK')
    NotFound = (404, 'Not Found')


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.buf_size = 1024

    def answer(self, proto, status, size=0):
        # GET / HTPP/1.1

        # HTPP/1.1 200 OK
        # Content-Length: 88 /r/n
        # /r/n
        # <html>
        result = [
            f'{proto} {status.code} {status.msg}'
        ]
        if size != 0:
            result.append(f'Content-Length: {size}\r\n')
        result.append('')
        return '\r\n'.join(result).encode()

    async def handle_client(self, con, addr):
        loop = asyncio.get_event_loop()
        logging.info(f'{addr} connected')
        with con:
            while True:
                data = await loop.sock_recv(con, self.buf_size)
                if not data:
                    break
                data = data.decode().splitlines()
                logging.debug(f'{data}')
                cmd = data[0]
                cmd = cmd.split()
                method = cmd[0]
                match method:
                    case 'GET':
                        path = cmd[1]
                        proto = cmd[2]
                        if path == '/':
                            path = '/index.html'
                        path = f'root{path}'
                        if os.path.isfile(path):
                            with open(path, 'rb') as file:
                                data = file.read()
                                answer = self.answer(proto, Status.OK, len(data))
                                answer += data
                        else:
                            answer = self.answer(proto, Status.NotFound)
                        # print(answer)
                        await loop.sock_sendall(con, answer)

                    # default:
                    case _:
                        pass
        logging.info(f'{addr} disconnected')

    async def run(self):
        loop = asyncio.get_event_loop()
        sock = socket.socket()
        sock.bind((self.host, self.port))
        sock.listen()
        logging.info(f'Server started')
        while True:
            con, addr = await loop.sock_accept(sock)
            # \n - NL New Line
            # \r - CR Carriage Return
            # Global Interpreter Lock
            # IO
            asyncio.create_task(self.handle_client(con, addr))
            # thread = threading.Thread(target=self.handle_client, args=(con, addr))
            # thread.start()

# Scheduler / Event Loop
# Task / Future
# Corutines
# async def f1():
#     print('A')
#     await asyncio.sleep(3)
#     print('B')
#
# async def f2():
#     print('C')
#     await asyncio.sleep(3)
#     print('D')

async def main():
    server = Server('127.0.0.1', 1234)

    await asyncio.create_task(server.run())
    # asyncio.start_server()
    #
    # await t1
    # await t2

# 127.0.0.1:1234
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    # asyncio.run(main())
    #
    # server = Server('127.0.0.1', 1234)
    # server.run()


import uuid

from deps.abc import Abstract


class Implementation(Abstract):
    def __init__(self):
        self.my_id = uuid.uuid4()
        print(self.my_id)

    def foo(self, z: int) -> str:
        return f'{self.my_id} : {z+1}'

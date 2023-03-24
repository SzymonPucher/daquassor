from starlette.responses import JSONResponse


class APIResponse(JSONResponse):
    def __init__(self, status_code, data=None, message=None, description=None):
        super().__init__(status_code=status_code)
        self.data = data
        self.message = message
        self.description = description

    @property
    def body(self):
        return self.render(
            dict(data=self.data, message=self.message, description=self.description)
        )

    @body.setter
    def body(self, val):
        self.__body = val

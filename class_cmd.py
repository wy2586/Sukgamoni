class Command:
    """
    커맨드를 클래스로 만들어보자.
    주의: 클래스 직접 선언이 아닌 @Command 데코레이터 형태로 사용해야 한다.
    실행할 함수는 void function(message message) 형태이다.
    :param name: 커맨드의 이름. 매 on_message가 실행되었을 때 content.startswith()로 검사한다.
    :param allowedChannel: 허용되는 채널의 이름.
    """
    def __init__(self, name, allowedChannel=None):
        assert name and (name != "")    # 이름이 비어있지 않다
        self.name = name.strip()        # 이름 앞뒤의 스페이스바를 제거
        self.allowedChannel = allowedChannel    # allowedChannel 설정(None일수도 있음)
        self.func = None                # self.func을 None로 설정(에러 방지)
        Commands.append(self)           # Commands 리스트에 이 커맨드를 등록


    def __call__(self, func):
        # 대체 왠지는 모르겠으나 데코레이터 처음 선언할때 이게 호출되더라
        if not self.func:
            self.func = func # 함수 변수를 할당해준다

        # 이 다음 줄은 나도 모름. 왜 있는거지?
        def wrapper(message):
            return func(message)
        return wrapper



    def checkMessage(self, message):
        """
        메세지가 이 커맨드를 호출한 것이 맞는지 확인만 한다.
        """
        # 메세지가 허용된 채널에 올라왔는가?
        if self.allowedChannel:
            if str(message.channel) != self.allowedChannel:
                return False

        # 메세지가 self.name의 값으로 시작하는가?
        return message.content.startswith(self.name)



    async def checkAndRun(self, message):
        """
        메세지에서 커맨드를 확인하고, 이 커맨드를 부른 게 맞다면 함수를 호출한다
        요약: on_message 이벤트에서 이 함수를 호출해 주세요
        """
        if self.checkMessage(message):
            await self.func(message)

# 커맨드 리스트
Commands = []
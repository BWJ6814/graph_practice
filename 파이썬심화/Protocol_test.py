from typing import Protocol

# 1. 프로토콜 정의 : find_path라는 함수만 있으면 내 동료다
class Router(Protocol):
    def find_path(self,start:tuple, end: tuple) -> list:
        '''
        
        '''

# 2. 상속없이 구현(클래스가 가볍고 자유로움)
class GeneticAlgorithmRouter:
    def find_path(self, start, end):
        print("GA 유전 알고리즘으로 다양한 경로 후보를 생성")
        return ["Gen_1", "Gen_2"]

# 3. 에이전트 코드
def run_ai_routing(router: Router, start: tuple, end: tuple):
    # router가 어떤 클래스든 상관 없이 find_path만 있으면 실행
    return router.find_path(start,end)

ga_router = GeneticAlgorithmRouter()
run_ai_routing(ga_router, (0,0),(5,5))

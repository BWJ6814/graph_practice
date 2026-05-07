'''
Abstract Base Class
규격을 먼저 정의하는 전통적인 방식
일반 상속보다 좀 더 강력함... 반드시 작성해야함
'''

from abc import ABC, abstractmethod

# 1. 모든 라우팅 알고리즘이 지켜야 할 표준 규격(추상클래스) 정의
class RoutingStrategy(ABC):
    @abstractmethod   
    def find_path(self, start: tuple, end: tuple, obstacles: list):
        # 이 메소드는 모든 전략 클래스에서 반드시 구현해야함
        pass

# 2. 전략 A: A* 알고리즘(빠른 경로 탐색)
class AStarRouting(RoutingStrategy):
    def find_path(self, start, end, obstacles):
        print(f"a* -> {start}에서 {end} 까지 최단 직성 경로 계산")
        return ["point1","point2"]

# 3. 전략 B: MILP 알고리즘 (복잡한 제약조건 최적화)
class MILPRouting(RoutingStrategy):
    def find_path(self, start, end , obstacles):
        print(f"milp -> {start}에서 {end} 까지 최단 직성 경로 계산")
        return ["Optimal_point1","Optimal_points2"]

# 4. 에이전트 (이 시스템을 사용하는 주체):
class RoutingAgent:
    def __init__(self, strategy: RoutingStrategy):
        self._strategy = strategy  # 현재 사용할 전략 저장

    def set_strategy(self, strategy: RoutingStrategy):
        self._strategy = strategy  # 도중에 전략 교체 가능
    
    def execute_routing(self, start, end): 
        # 구체적 알고리즘은 구현
        return self._strategy.find_path(start, end, [])
    
agent = RoutingAgent(AStarRouting())
agent.execute_routing((0,0),(10,10)) # A* 실행

agent.set_strategy(MILPRouting())
agent.execute_routing((0,0),(10,10))
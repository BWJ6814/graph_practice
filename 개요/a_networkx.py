'''
P&ID는 설비의 논리적 흐름을 보여줌. 이를 Python의 networkx 라이브러리로 모델링하는 코드 예시
'''
import networkx as nx

# 1. 그래프 객체 생성 (배관은 흐름이 있으니깐 방향 그래프 DiGraph)
G = nx.DiGraph()

# 2. 노드 추가
G.add_node("A", type="Pump", tag="P-101")
G.add_node("B", type="Valve", tag="V-201")
G.add_node("C", type="Pressure Gauge", tag="PG-301")
G.add_node("D", type="Tank", tag="T-401")

# 3.엣지 추가 및 속성 설정(배관의 길이, 재질 등을 속성으로 저장)  이게 가중치 그래프? 인듯?
G.add_edge("A","B", length=10, unit="m",material="Stainless Steel")
G.add_edge("B","C", length=2, unit="m",material="Stainless Steel")
G.add_edge("C","D", length=5, unit="m",material="Stainless Steel")

# 속성 확인 예시
print(f"장비 A의 종류 : {G.nodes['A']['type']}")
print(f"A에서 B 사이 배관 길이 : {G['B']['C']['length']}m")   # c -> b 는 안됨 아마 방향그래프라서?

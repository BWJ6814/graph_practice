'''
이 모듈은 A* 알고리즘이 다양한 상황 에서 최단 거리를 잘 찾는지 자동으로 검사합니다
'''

import pytest

# 테스트할 가상의 알고리즘 함수
def a_star_routing(graph,start,end):
    # 테스트를 위해 간단한 거리 계산 로직(실제로는 복잡한 a*가 들어감)
    if start not in graph or end not in graph : return None
    return len(graph)


# 1. Fixture: 공통으로 사용할 '공장 도면(그래프)' 데이터 준비
@pytest.fixture
def factory_map():
    return {
        "Simple": {"A": ["B"], "B": ["C"], "C": []},
        "Complex": {"A": ["B", "D"], "B": ["C"], "D": ["C"], "C": []}
    }

# 2. Parametrize: 여러 케이스를 한 번에 테스트
@pytest.mark.parametrize("map_type, start, end, expected_exists", [
    ("Simple", "A", "C", True),
    ("Simple", "A", "Z", True), # 없는 장비
    ("Complex", "A", "C", True)
])
def test_a_star_pathfinding(factory_map, map_type, start, end, expected_exists):
    path = a_star_routing(factory_map[map_type], start, end)
    
    if expected_exists:
        assert path is not None
    else:
        assert path is None
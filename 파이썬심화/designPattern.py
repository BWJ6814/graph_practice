'''
# 스파게티 코드

def get_affected_lines(equipment_id, all_data):
    # 데이터 파싱, 필터링, 로직이 한 함수에 다 있음
    affected = []
    for item in all_data:
        if item['type'] == 'LINE':
            if item['source'] == equipment_id or item['target'] == equipment_id:
                # 복잡한 비즈니스 로직 (예: 가스관인 경우 특정 압력 이상만 추출)
                if item['fluid'] == 'GAS' and item['pressure'] > 5.0:
                    affected.append(item)
                elif item['fluid'] == 'WATER':
                    affected.append(item)
    return affected

'''

from pydantic import BaseModel
from abc import ABC, abstractmethod

# 1. 데이터 모델 (도메인 객체)
class Line(BaseModel):
    id: str
    source: str
    target: str
    fluid: str
    pressure: float

# 2. 영향력 분석 전략 (Strategy 패턴)
class ImpactStrategy(ABC):
    @abstractmethod
    def is_affected(self, line: Line, eq_id: str) -> bool: pass

class GasImpact(ImpactStrategy):
    def is_affected(self, line, eq_id):
        return (line.source == eq_id or line.target == eq_id) and line.pressure > 5.0

# 3. 메인 분석기 (비즈니스 로직과 데이터 분리)
class FlowAnalyzer:
    def __init__(self, strategy: ImpactStrategy):
        self.strategy = strategy

    def analyze(self, lines: list[Line], eq_id: str):
        return [l for l in lines if self.strategy.is_affected(l, eq_id)]
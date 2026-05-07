from pydantic import BaseModel, Field, field_validator
from typing import Literal, Union, List

# --- 1. 배관 모델 정의 ----
# BaseModel 넣는 순간 -> 단순한 클래스가 아니라 "데이터 검증 기능이 있는 모델" 선언
# 주요 기능 "데이터 타입 체크", "Json 변환", "에러 메세지 생성"
class PipeEdge(BaseModel): 
    source_id: str # 시작 장비 ID
    target_id: str # 끝 장비 ID
    # field -> 변수에 대해 더 세부적인 설정(메타데이터)을 하기 위해 사용
    # ... -> 파이썬에서 생략을 뜻하지만 pydatic 에서는 "이값은 필수 항목이라는 뜻"
    # description -> 주석
    length: float = Field(..., description="배관 길이(m)")
    presure: float = Field(..., description="설계 압력(bar)")
    material: str = Field("Stainless Steel", description="설계 압력(bar)")

    # [자동 검증 로직] 배관 길이는 0보다 커야 함
    # 아래에 있는 함수를 length 필드를 검사하는 용도로 써라
    # classmethod field_validator는 클래스 자체에서 동작해야함
    # @ -> 데코레이터  , -> float: 리턴 타입 힌트 [가독성 땜에]
    @field_validator('length')
    @classmethod
    def validate_length(cls, v: float) -> float:
        if v <= 0:
            # raise -> 여기에서 의도적으로 에러를 발생 시키겠다 (ex) 길이가 음수일때)
            # ValueError 내장 에러 종류 타입은 맞지만 숫자 나 값이 적절하지 않다
            raise ValueError("배관 길이는 0보다 커야합니다. (물리적 불가능)")
        return v
    

# --- 2. 장비 (노드) 종류별 모델 정의 ---
class BaseNode(BaseModel):
    id: str = Field(..., description="장비 고유 식별자")
    tag_name: str = Field(..., description="도면상의 태그 번호 (예: P-101)")

class PumpNode(BaseNode):
    node_type: Literal["PUMP"] = "PUMP"
    capacity: float = Field(..., description="유량 (m³/h)")

class ValveNode(BaseNode):
    node_type: Literal["VALVE"] = "VALVE"
    valve_type: str = Field(..., description="밸브 종류 (예: Gate, Ball)")

class InstrumentNode(BaseNode):
    node_type: Literal["INSTRUMENT"] = "INSTRUMENT"
    measurement: str = Field(..., description="측정 항목 (예: Pressure, Temp)")

# --- 3. 전체 P&ID 그래프 데이터 모델 ---
class PIDGraph(BaseModel):
    # 다양한 노드 타입을 하나로 묶음
    nodes: List[Union[PumpNode, ValveNode, InstrumentNode]]
    edges: List[PipeEdge] 
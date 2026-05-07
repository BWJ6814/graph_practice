from fastapi import FastAPI
import asyncio

app = FastAPI()

# 디노 AI 에이전트가 설계를 판단한다고 가정하는 비동기 함수
# 기능 덧붙이기
@app.get("/d-inno/ai-agent")
async def run_ai_agent(request_text: str):
    # 'asyncio'를 이용해 2초 동안 AI가 설계(그래프 DB 조회 등)를 한다고 가정함
    print(f"주문 받음: {request_text}")
    await asyncio.sleep(2) 
    
    # 디노의 도메인 지식을 반영한 가짜 응답[cite: 1, 2]
    return {
        "status": "success",
        "agent_decision": f"'{request_text}' 요청에 따라 배관 경로 정합성 검증 완료",
        "result": "설계와 시공 데이터가 99.8% 일치합니다."
    }
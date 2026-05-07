import asyncio
import time

'''
커리큘럼에서 강조하는 asyncio, await 같은 비동기 문법의 실전 종착역이 
바로 uvicorn 위에서 돌아가는 웹 서비스입니다.
AI 모델이 '뇌'라면, FastAPI 같은 프레임워크는 '입'이고, uvicorn은 이 소리가 멀리 퍼지게 
해주는 '마이크'입니다.
'''

# 1. 동기 방식 테스트 (서버 응답을 기다리느라 멈춤)
def sync_task(i):
    print(f"동기 작업 {i} 시작...")
    time.sleep(0.5)  # 0.5초 동안 아무것도 못하고 멈춤
    return f"결과 {i}"

# 2. 비동기 방식 테스트 (기다리는 동안 다른 일을 함)
async def async_task(i, semaphore):
    async with semaphore:
        print(f"비동기 작업 {i} 요청 전송...")
        await asyncio.sleep(0.5)  # 0.5초 기다리지만, 그 사이 다른 작업이 시작됨
        print(f"비동기 작업 {i} 완료!")
        return f"결과 {i}"

async def main():
    # --- 비동기 테스트 실행 ---
    print("--- 비동기 방식 시작 ---")
    start = time.perf_counter()
    semaphore = asyncio.Semaphore(10)
    tasks = [async_task(i, semaphore) for i in range(100)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"비동기 총 소요 시간: {end - start:.2f}초")

    # --- 동기 테스트 실행 (10개만 테스트해도 오래 걸림) ---
    print("\n--- 동기 방식 시작 (10개만 실행) ---")
    start = time.perf_counter()
    for i in range(10):
        sync_task(i)
    end = time.perf_counter()
    print(f"동기 총 소요 시간 (10개 기준): {end - start:.2f}초")

if __name__ == "__main__":
    asyncio.run(main())
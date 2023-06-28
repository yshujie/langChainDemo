import asyncio
import time 

from src.case.chains import (
    namer,
    anamer
)

def testANamer():
    s = time.perf_counter()
    asyncio.run(anamer.generate_concurrently())
    elapsed = time.perf_counter() - s
    print("\033[1m]" + f"Concurrent execution in {elapsed:0.2f} seconds.\033[0m")
    
    s = time.perf_counter()
    anamer.generate_serially()
    elapsed = time.perf_counter() - s
    print("\033[1m]" + f"Serial execution in {elapsed:0.2f} seconds.\033[0m")

    
if __name__ == "__main__":
    testANamer()
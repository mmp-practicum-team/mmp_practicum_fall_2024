import asyncio

# co-routine function
async def my_task(duration):
    await asyncio.sleep(duration)
    return f"Slept for {duration} seconds"

# create and execute tasks
async def main():
    tasks = [my_task(2), my_task(1), my_task(3)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    results = asyncio.run(main())
    print(results)
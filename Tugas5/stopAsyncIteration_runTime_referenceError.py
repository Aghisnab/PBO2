print("Runtime Error")
try:
    def divide(a,b):
        try:
            result = a / b
            return result
        except:
            raise RuntimeError("An Error Occured")
    print(divide(9, 2))
    print(divide(12, 0))
except RuntimeError as e:
    print(e)

print("\nReference Error")
try:
    import gc as g
    import weakref as wk
    class check_object(object):
        def __init__(self,name):
            self.name = name
        def __del__(self):
            print('Delete it %s')%self
    print('Reference Object = ',a.name)   
except NameError:
    print('Reference Object No Longer Exist')

print("\nStop Async Iteration")
try:
    import asyncio
    async def async_generator():
        for i in range(5):
            await asyncio.sleep(2)
            yield i

    async def main():
        async for item in async_generator():
            print(item)
    asyncio.run(main())
except KeyboardInterrupt:
    print("Iteration Stopped by User!")



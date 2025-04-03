import asyncio
import mcpimageprocessing

async def main():
    await mcpimageprocessing.save_image(
        image_source="https://images.myguide-cdn.com/bordeaux/companies/la-tupina/large/la-tupina-343880.jpg",
        output_path="/Users/fengjinchao/Desktop/new_image_pro/mcpimageprocessing/1.jpg",
    )

# 运行异步主函数
asyncio.run(main())

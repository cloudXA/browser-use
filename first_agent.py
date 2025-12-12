'''
Author: zhangxiang davieas.zhang@derbysoft.net
Date: 2025-11-11 14:56:09
LastEditors: zhangxiang davieas.zhang@derbysoft.net
LastEditTime: 2025-12-04 11:17:56
FilePath: /browser-use/first_agent.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''使用browser-use的简单示例'''
from browser_use import Agent, ChatBrowserUse, Browser
import asyncio

async def example():
    try:
        print("正在创建browser-use agent...")
        # 创建浏览器实例并设置keep_alive=True来保持浏览器打开
        browser = Browser(keep_alive=True)
        
        # 使用默认配置创建agent，不指定复杂的浏览器配置
        agent = Agent(
            task="帮我搜集AI漫剧的教程",
            llm=ChatBrowserUse(),
            browser=browser
        )
        
        print("执行任务...")
        # 运行agent
        history = await agent.run()
        
        print(f"\n🎉 任务完成！")
        # 浏览器会保持打开状态，直到手动关闭
        print("浏览器保持打开状态，您可以继续使用。")
        return [history]
        
    except Exception as e:
        print(f"❌ 执行过程中出现错误: {e}")
        import traceback
        traceback.print_exc()
        return []

if __name__ == "__main__":
    histories = asyncio.run(example())
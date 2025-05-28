{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4ee2c57d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'stock_info'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlangchain\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mprompts\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m ChatPromptTemplate\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstock_info\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Stock\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlangchain_core\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01moutput_parsers\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m StrOutputParser\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlangchain_openai\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m ChatOpenAI\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'stock_info'"
     ]
    }
   ],
   "source": [
    "from langchain.prompts import ChatPromptTemplate\n",
    "from stock_info import Stock\n",
    "from langchain_core.output_parsers import StrOutputParser\n",
    "from langchain_openai import ChatOpenAI\n",
    "\n",
    "def invesment_report(company:str, symbol:str) -> str:\n",
    "    prompt = ChatPromptTemplate.from_messages([\n",
    "        (\"system\", \"\"\"\n",
    "            Want assistance provided by qualified individuals enabled with experience on understanding charts \n",
    "            using technical analysis tools while interpreting macroeconomic environment prevailing across world \n",
    "            consequently assisting customers acquire long term advantages requires clear verdicts therefore \n",
    "            seeking same through informed predictions written down precisely! First statement contains \n",
    "            following content- \"Can you tell us what future stock market looks like based upon current conditions ?\".\n",
    "        \"\"\"),\n",
    "        (\"user\", \"\"\"\n",
    "            {company} 주식에 투자해도 될까요?\n",
    "            아래의 기본정보, 재무제표를 참고해 마크다운 형식의 투자보고서를 한글로 작성해 주세요.\n",
    "        \n",
    "            기본정보:\n",
    "            {basic_info}\n",
    "        \n",
    "            재무제표:\n",
    "            {financial_statement}\n",
    "\n",
    "        \"\"\")\n",
    "    ])\n",
    "\n",
    "    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)\n",
    "\n",
    "    chain = prompt | llm | StrOutputParser()   \n",
    "    \n",
    "    stock = Stock(symbol)\n",
    "    result = chain.invoke({\n",
    "        \"company\": company,\n",
    "        \"basic_info\": stock.get_basic_info(),\n",
    "        \"financial_statement\": stock.get_financial_statement()\n",
    "    })\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2221e05",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "llm.venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# grisha_key="sk-proj-m19aOPEP6juwwvdULE1DOqGvBeTkRvf0WDdgjCzTj1LCpfp9_XzY4fnH3zI4xtK1PtUzhf24dLeqPT3BlbkFJMNMkTDgOLKvnx-i0XqApRX0d06dhAH5fak6lWWBdIFY-7yr-QgT7dlPXbwHl8tfke8paNpPawA111"

import os
os.environ["OPENAI_API_KEY"]=grisha_key

llm=OpenAI()

def generate_gestaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a resturant for {cuisine} food.suggest a fency name for this"
    )
    # prompt_template_name.format(cuisine="Indian")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    # name_chain.run("Indian"
    # chain.run("Indian")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name} Return is by comma seprated list"
    )
    # prompt_template_items.format(restaurant_name="Indian")

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response=chain({'cuisine':cuisine})
    return response


if __name__=="__main__":
    print(generate_gestaurant_name_and_items("Italian"))

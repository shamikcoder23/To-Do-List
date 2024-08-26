import streamlit as st
import time
from streamlit_extras.stylable_container import *
import pandas as pd
from todo_database import *


def main () :
	with stylable_container(
        key="title",
        css_styles="""
	        {
              	background-color: yellow;
               	border-radius: 15px;
				text-align: center,
				border: 5px solid red;
               	border-radius: 0.5rem;
               	padding: 0 calc(1em - 1px) calc(1em - 1px)
           	}
        	""",
	):
		st.title(':blue[Your Personal _To-Do List_] 📋')
	st.subheader(":blue[Choose from the available options:]")

	dropdown = ["Add to list ✍🏻", "Edit list 🗂️", "Delete from list ❌"]
	dropview = ["View list 👀"]
	cola, colb = st.columns([1, 1])
	choice = cola.selectbox("Option 1: Work with your list", dropdown)
	c = colb.selectbox("Option 2: View your list", dropview)

	st.divider()
		#st.info("You have chosen : {}".format(choice))
	if c == "View list 👀":
		view()
	
	id_drop = []
	if choice == "Add to list ✍🏻":
		col1, col2 = st.columns([1, 1])
		task = col1.text_input("Add task")
		due = col2.date_input("Set Due Date")
		pri = col1.slider("Set Priority: ('1' is minimum, '10' is maximum)", min_value=1, max_value= 10)

		if st.button("Add") :
			if task == "":
				st.error("Please add task")
			else:
				#id_drop.append(id)
				add(task, pri, due)
				st.divider()					
				time.sleep(2)
				st.success("Task added successfully ✅")
			
					#view()

	if choice == "Edit list 🗂️":
		if len(to_do_list) == 0:
			st.warning("Table is empty. Nothing to edit")
		else:
			for i in range(len(to_do_list)):
				id_drop.append(i)
			col1, col2 = st.columns([1, 1])
			i = col1.selectbox("Enter id to edit", id_drop)
			task = col2.text_input("Edit task")
			pri = col1.slider("Edit Priority: ", min_value=1, max_value= 10)
			due = col2.date_input("Edit Due Date")

			if st.button("Confirm changes") :
				if task == "" :
					st.error("Please add task")
				else:
					update(i, task, pri, due)
					st.divider()					
					time.sleep(2)
					st.success("Task edited successfully ✅")
					#view()
	
	if choice == "Delete from list ❌":
		if len(to_do_list) == 0:
			st.warning("Table is empty. Nothing to delete")
		else:
			for i in range(len(to_do_list)):
				id_drop.append(i)
			i = st.selectbox("Enter id to edit", id_drop)
			if to_do_list[i][1] >= 3 and to_do_list[i][1] <= 6 :
				st.warning("🤔 This is a medium priority task, delete with caution 🤔")
			elif to_do_list[i][1] > 6 :
				st.warning("😨 This is a high prority task, do you really want to delete it? 😨")

			if st.button("Confirm") :
				delete(i)
				st.divider()					
				time.sleep(2)
				st.success("Task deleted successfully ✅")
	# with stylable_container(
	# 	key="main",
	# 	css_styles="""
	# 		{
	# 			color: blue,
	# 			width: 105px
	# 		}
	# 	"""
	# ):
		


if __name__ == '__main__' :
	main()
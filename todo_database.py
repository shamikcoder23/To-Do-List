import pandas as pd
import streamlit as st
import matplotlib as mp

to_do_list = []

def view () :
	if len(to_do_list) == 0:
		st.warning("List is empty ! Add tasks to view")
		return
	to_do_list.sort(reverse=True, key=lambda x : x[1])
	df = pd.DataFrame(to_do_list, columns=["Task to Perform", "Priority", "Final Deadline"])
	#df.style.highlight_max(subset=["Priority"], axis=0)
	# df.style.background_gradient(axis=None, cmap='YlOrRd', subset=['Priority'])
	return st.dataframe(df.style.background_gradient(axis=None, cmap='YlOrRd', subset=['Priority']))	

def add (task, pri, due) :
	lst = [task, pri, due]
	to_do_list.append(lst)

def update (id, task, pri, due):	
	to_do_list[id] = [task, pri, due]

def delete (id) :
	to_do_list.pop(id)
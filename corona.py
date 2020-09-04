import tkinter as tk
import requests
import json
import tkinter.font as tkfont






#getting data from the site
API_KEY = "tuq37i3Tn2bK"
PROJECT_TOKEN = "tWHaXZ6-oqqT"
RUN_TOKEN = "t9zbMMkHCsN0"


class data():
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.get_data()

	def get_data(self):
		r = requests.post(f"https://www.parsehub.com/api/v2/projects/{self.project_token}/run", data = self.params)
		request = requests.get(f"https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data", params = self.params)
		self.data = json.loads(request.text)


Data = data(API_KEY, PROJECT_TOKEN)









#The GUI app
country = None
required_country = None
click_enter = 0

cases_label = 0
deaths_label = 0
newcases_label = 0
newdeaths_label = 0
wrong_input = 0
not_available = 0



#Enter function
def enter():
	
	global country
	global click_enter
	global cases_label
	global deaths_label
	global newcases_label
	global newdeaths_label
	global wrong_input 
	global not_available

	country = country_search.get()

	if click_enter == 1:
		cases_label.destroy()
		deaths_label.destroy()
		newcases_label.destroy()
		newdeaths_label.destroy()

	if wrong_input == 1:
		not_available.destroy()


	if country.lower() == "all":
		required_country = Data.data['total']

		for content in required_country:
			if content['name'] == 'Coronavirus Cases:':
				number_of_cases = "total cases: " + content['value']

			if content['name'] == 'Deaths:':
				number_of_deaths = "total deaths: " + content['value']

		number_of_newcases = ""
		number_of_newdeaths = "" 

		font3 = tkfont.Font(size = 15, weight = "bold")
		cases_label = tk.Label(frame, text = number_of_cases, bg = "Navy Blue", fg = "White", font = font3)
		deaths_label = tk.Label(frame, text = number_of_deaths, bg = "Navy Blue", fg = "White", font = font3)
		newcases_label = tk.Label(frame, text = number_of_newcases, bg = "Navy Blue", fg = "White", font = font3)
		newdeaths_label = tk.Label(frame, text = number_of_newdeaths, bg = "Navy Blue", fg = "White", font = font3)

		cases_label.place(relx = 0.25 ,rely = 0.3)
		deaths_label.place(relx = 0.25 ,rely = 0.4)
		newcases_label.place(relx = 0.25 ,rely = 0.5)
		newdeaths_label.place(relx = 0.25 ,rely = 0.6)


	else:
		required_country = Data.data['countries']

		for content in required_country:
			if content['name'].lower() == country.lower():
				number_of_cases = "total cases: " + content['total_cases']
				number_of_deaths = "total deaths: " + content['total_deaths']
				number_of_newcases = "new cases: " + content['new_cases']
				number_of_newdeaths = "new deaths: " + content['new_deaths']

				font3 = tkfont.Font(size = 20, weight = "bold")
				cases_label = tk.Label(frame, text = number_of_cases, bg = "Navy Blue", fg = "White", font = font3)
				deaths_label = tk.Label(frame, text = number_of_deaths, bg = "Navy Blue", fg = "White", font = font3)
				newcases_label = tk.Label(frame, text = number_of_newcases, bg = "Navy Blue", fg = "White", font = font3)
				newdeaths_label = tk.Label(frame, text = number_of_newdeaths, bg = "Navy Blue", fg = "White", font = font3)

				cases_label.place(relx = 0.25 ,rely = 0.3)
				deaths_label.place(relx = 0.25 ,rely = 0.4)
				newcases_label.place(relx = 0.25 ,rely = 0.5)
				newdeaths_label.place(relx = 0.25 ,rely = 0.6)
				click_enter = 1
				wrong_input = 0

				break

			elif content == required_country[-1] and content['name'].lower() != country.lower():

				font = tkfont.Font(size = 15, weight = "bold")
				not_available = tk.Label(frame, text = "THE COUNTRY YOU ENTERED DOES NOT EXIST!", bg = "Navy Blue", fg = "Red", font = font)
				not_available.place(rely = 0.7, relx = 0.1)
				click_enter = 0
				wrong_input = 1

		




#making the window
root = tk.Tk()
root.title("corona-live")
root.geometry("800x450")

#adding a background image
bgimage = tk.PhotoImage(file = "coronaimage.png")
bglabel = tk.Label(root, image = bgimage)
bglabel.place(relheight = 1, relwidth = 1)

#making a frame
frame = tk.Frame(root, bg = "Navy Blue")
frame.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)

#Taking an input with entry and a button
country_search = tk.Entry(frame)
country_search.place(rely = 0.2, relx = 0.2, relwidth = 0.43, height = 25)

enter_button = tk.Button(frame, text = "Enter", bg = "Grey", fg = "Black", command = enter)
enter_button.place(relwidth = 0.1, height = 25, relx = 0.65, rely = 0.2)

#header
font2 = tkfont.Font(size = 25, weight = "bold")
header = tk.Label(root, text = "Corona-Live", bg = "Red", fg = "White", font = font2)
header.place(relx = 0.35)

#A small note from my side
font1 = tkfont.Font(size = 9)
disclaimerLabel = tk.Label(root, text = "Please run this program again after 10 min to get a more accurate info", bg = "Black", fg = "White", font = font1)
disclaimerLabel.place(relx = 0.25, rely = 0.9)

disclaimerLabel2 = tk.Label(root, text = "To get the total number of cases in the world, type 'all'", bg = "Black", fg = "White", font = font1)
disclaimerLabel2.place(rely = 0.95, relx = 0.3)


tk.mainloop()

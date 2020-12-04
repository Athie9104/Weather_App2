
# Author ATHENKOSI GONGOTHA
from tkinter import*
from tkinter import messagebox

# function for the (check) weather button
def state_weather():
    import requests, json

    #API KEY
    weather_key = 'b2a0e923e0b5f768b7c6561f0f7398d2'

    #url
    url = 'https://api.openweathermap.org/data/2.5/weather'

    #City name from city text box
    city_name = Ecity.get()
    params1 = {'appid':weather_key, 'q': 'Cape Town', 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()

    if weather['cod'] != '404':
        y=weather['main']
        current_temp=y['temp']
        current_presre=y['pressure']
        current_humid=y['humidity']
        z=weather['weather']
        weather_descript= z[0]['description']
        Etemp.insert(15, str(current_temp)+ "" +'Degrees') # displaying current temperature
        Eatm.insert(10, str(current_presre)+ "" +'hPa') # Displaying current pressure
        Ehumid.insert(15, str(current_humid)+ "" +'%') # Displaying current humidity
        Edescrit.insert(10, str(weather_descript))
    else:
        messagebox.showerror('Error', 'City not found \n'
                             'Please enter a valid City') # if you have entered incorrect name for the city
        Ecity.delete(0, END) # clearing the city text box


def clear1(): # function for the clear button
    Ecity.delete(0, END)
    Etemp.delete(0, END)
    Eatm.delete(0, END)
    Ehumid.delete(0,END)
    Edescrit.delete(0, END)

    Ecity.focus_set() # setting focus to the (enter city) text box

if __name__ == "__main__":

    root = Tk()
    root.geometry('495x180')
    root.config(bg='blue')
    root.title('Weather app')

    Ecity = Entry(root, text='Enter city', width=40)
    Etemp = Entry(root, width=40)
    Eatm = Entry(root, width=40)
    Ehumid = Entry(root, width =40)
    Edescrit = Entry(root, width=40)
    Ecity.grid(column=1, row=0), Etemp.grid(column=1, row=1), Eatm.grid(column=1, row=4), Ehumid.grid(column=1, row=5) ,Edescrit.grid(column=1, row=6)

    lbl_city = Label(root, text='City', width=20, bg='blue', fg='white')
    lbl_temp = Label(root, text='Temperature', width=20, bg='blue', fg='white')
    lbl_atm = Label(root, text='Atmospheric pressure', width=20, bg='blue', fg='white')
    lbl_humid = Label(root, text='Humidity', width=20, bg='blue', fg='white')
    lbl_descript = Label(root, text='Description', width=20, bg='blue', fg='white')
    lbl_city.grid(column=0, row=0), lbl_temp.grid(column=0, row=1), lbl_atm.grid(column=0, row=4), lbl_humid.grid(column=0, row=5), lbl_descript.grid(column=0, row=6)

    btn_subm = Button(root, text='Check', width=10, bg='black', fg='white', command=state_weather)
    btn_clear = Button(root, text=' Clear', width=10, bg='black', fg='white', command=clear1)
    btn_subm.grid(column=1, row=2), btn_clear.grid(column=1, row=7)

    root.mainloop()


# import requests
#
# url = 'https://api.openweathermap.org/data/2.5/weather'
# weather_key = 'b2a0e923e0b5f768b7c6561f0f7398d2'
# params1 = {'appid':weather_key, 'q': 'Cape Town', 'units': 'Metric'}
#
# response = requests.get(url, params=params1)
#weather = response.json()
# print(weather)
# print(weather['wind']['speed'])

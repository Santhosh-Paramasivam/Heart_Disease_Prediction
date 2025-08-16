import pickle
import tkinter as tk
import customtkinter
from PIL import Image


def isfloat(str):
    if str.count('.') != 1:
        return False
    str_dot_removed = str.replace('.', '')
    if str_dot_removed.isnumeric():
        return True
    else:
        return False


class HeartDiseasePrediction(customtkinter.CTk):

    def __init__(self):

        customtkinter.CTk.__init__(self)
        self.geometry('900x666')
        self.title('Heart Disease Prediction')
        self.iconbitmap(bitmap='icon.ico')

        self.model_load()
        self.font_load()
        self.background_place()
        self.place_entries()
        self.place_combos()
        self.place_radios()
        self.place_empty_errors()
        self.place_button()

    def font_load(self):

        self.Noto_Serif = customtkinter.CTkFont(family='Noto Serif', size=12)
        self.Aileron = customtkinter.CTkFont(family='Aileron', size=16)
        self.Gotham = customtkinter.CTkFont(family='Gotham-Bold', size=19)

    def model_load(self):

        with open('LogModel.pickle', 'rb') as infile:
            self.model = pickle.load(infile)

        with open('Input_Series.pickle', 'rb') as infile:
            self.Input = pickle.load(infile)

        with open('Storage_DF.pickle', 'rb') as infile:
            self.Storage = pickle.load(infile)

    def background_place(self):

        self.Background_Frame = customtkinter.CTkFrame(self, border_color='#0C1765')
        self.Background_Frame.grid(row=1, column=0)

        background_image = customtkinter.CTkImage(light_image=Image.open('Background.png'), dark_image=Image.open('Background.png'), size=(900, 675))
        background_label = customtkinter.CTkLabel(self.Background_Frame, image=background_image, text='')
        background_label.pack()

    def place_entries(self):

        self.Age_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='in years',
                                                border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.Age_Entry.place(x=210, y=425)

        self.RestingBP_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='in mm Hg',
                                                      border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.RestingBP_Entry.place(x=210, y=547)

        self.Cholesterol_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='in mm/dl',
                                                        border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.Cholesterol_Entry.place(x=671, y=74)

        self.FastingBS_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='in mg/dl',
                                                      border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.FastingBS_Entry.place(x=671, y=132)

        self.MaxHR_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='in bpm',
                                                  border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.MaxHR_Entry.place(x=671, y=326)

        self.Oldpeak_Entry = customtkinter.CTkEntry(self.Background_Frame, corner_radius=8, fg_color='white', placeholder_text='',
                                                    border_color='grey', border_width=1, width=172, height=28, bg_color=('#FFFFFF', '#FFFFFF'))
        self.Oldpeak_Entry.place(x=671, y=374)

    def place_combos(self):

        self.ChestPainType_options = [
            'Asymptomatic', 'Non-Anginal Pain', 'Atypical Angina', 'Typical Angina']
        self.ChestPainType_Var = customtkinter.StringVar()
        self.ChestPainType_Var.set(self.ChestPainType_options[0])
        self.ChestPainType_Combo = customtkinter.CTkComboBox(self.Background_Frame, corner_radius=8, fg_color='white', border_color='grey', border_width=1, 
                                                             width=172, height=28, bg_color=('white', 'white'), values=self.ChestPainType_options, variable=self.ChestPainType_Var, dropdown_fg_color='white')
        self.ChestPainType_Combo.place(x=210, y=482)

        self.RestingECG_options = [
            'Normal', 'Left Ventricular Hypertrophy', 'ST-T Wave Abnormality']
        self.RestingECG_Var = customtkinter.StringVar()
        self.RestingECG_Var.set(self.RestingECG_options[0])
        self.RestingECG_Combo = customtkinter.CTkComboBox(self.Background_Frame, corner_radius=8, fg_color='white', border_color='grey', border_width=1, width=172, 
                                                          height=28, bg_color=('white', 'white'), values=self.RestingECG_options, variable=self.RestingECG_Var, dropdown_fg_color='white')
        self.RestingECG_Combo.place(x=671, y=199)

        self.STSlope_options = ['Flat', 'Upsloping', 'Downsloping']
        self.STSlope_Var = customtkinter.StringVar()
        self.STSlope_Var.set(self.STSlope_options[0])
        self.STSlope_Combo = customtkinter.CTkComboBox(self.Background_Frame, corner_radius=8, fg_color='white', border_color='grey', border_width=1, 
                                                       width=172, height=28, bg_color=('white', 'white'), values=self.STSlope_options, variable=self.STSlope_Var, dropdown_fg_color='white')
        self.STSlope_Combo.place(x=671, y=425)

    def place_radios(self):

        self.Sex_Var = customtkinter.StringVar()
        self.Sex_Var.set('Male')
        self.Male_Button = customtkinter.CTkRadioButton(self.Background_Frame, variable=self.Sex_Var, value='Male', radiobutton_height=12, radiobutton_width=12, text='',
                                                        bg_color='white', width=0, height=0, border_color='#929291', border_width_unchecked=2, border_width_checked=4, fg_color='#345CBB', hover_color='#527DDF')
        self.Male_Button.place(x=216, y=377)
        self.Female_Button = customtkinter.CTkRadioButton(self.Background_Frame, variable=self.Sex_Var, value='Female', radiobutton_height=12, radiobutton_width=12, text='',
                                                          bg_color='white', width=0, height=0, border_color='#929291', border_width_unchecked=2, border_width_checked=4, fg_color='#345CBB', hover_color='#527DDF')
        self.Female_Button.place(x=296, y=377)

        self.ExerciseAngina_Var = customtkinter.StringVar()
        self.ExerciseAngina_Var.set('Yes')
        self.Yes_Button = customtkinter.CTkRadioButton(self.Background_Frame, radiobutton_height=12, variable=self.ExerciseAngina_Var, value='Yes', radiobutton_width=12, text='',
                                                       bg_color='white', text_color='#AFAFAF', width=0, height=0, border_color='#929291', border_width_unchecked=2, border_width_checked=4, fg_color='#345CBB', hover_color='#6B8CD6')
        self.Yes_Button.place(x=691, y=270)
        self.No_Button = customtkinter.CTkRadioButton(self.Background_Frame, radiobutton_height=12, variable=self.ExerciseAngina_Var, value='No', radiobutton_width=12, text='',
                                                      bg_color='white', text_color='#AFAFAF', width=0, height=0, border_color='#929291', border_width_unchecked=2, border_width_checked=4, fg_color='#345CBB', hover_color='#6B8CD6')
        self.No_Button.place(x=776, y=270)

    def place_empty_errors(self):

        self.Age_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.ChestPainType_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.RestingBP_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.Cholesterol_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.FastingBS_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.MaxHR_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.Oldpeak_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.RestingECG_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.STSlope_Error = customtkinter.CTkLabel(self.Background_Frame)

    def prepare_Sex(self):

        Map_Sex = {'Male': 1, 'Female': 0}
        Sex = float(Map_Sex[self.Sex_Var.get()])
        return Sex

    def prepare_Age(self):

        Age_Var = self.Age_Entry.get()

        if (Age_Var == '') or (Age_Var.isnumeric() != True):
            self.Age_Error.destroy()
            self.Age_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif,
                                                    text='Enter an integer value!', bg_color='white', fg_color='white', width=0, height=0)
            self.Age_Error.place(x=230, y=454.5)
            self.ML_Pass = False
            return

        self.Age_Error.destroy()
        self.Age_Error = customtkinter.CTkLabel(self.Background_Frame)
        Age = float(Age_Var)
        return Age

    def prepare_ChestPainType(self):

        Map_ChestPainType = {'Asymptomatic': 4, 'Non-Anginal Pain': 3,
                             'Atypical Angina': 2, 'Typical Angina': 1}

        ChestPainType_Var2 = self.ChestPainType_Var.get()
        ChestPainType_Var2 = ChestPainType_Var2.strip()

        if ChestPainType_Var2 not in self.ChestPainType_options:
            self.ChestPainType_Error.destroy()
            self.ChestPainType_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif, text='Enter a valid option!', 
                                                              bg_color='white', fg_color='white', width=0, height=0)
            self.ChestPainType_Error.place(x=236, y=511)
            self.ML_Pass = False
            return

        self.ChestPainType_Error.destroy()
        self.ChestPainType_Error = customtkinter.CTkLabel(self.Background_Frame)
        ChestPainType = float(Map_ChestPainType[ChestPainType_Var2])
        return ChestPainType

    def prepare_RestingBP(self):

        RestingBP_Var = self.RestingBP_Entry.get()

        if (RestingBP_Var == '') or ((RestingBP_Var.isnumeric() != True) and (isfloat(RestingBP_Var) != True)):
            self.RestingBP_Error.destroy()
            self.RestingBP_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif, text='Enter a numeric value!', 
                                                          bg_color='white', fg_color='white', width=0, height=0)
            self.RestingBP_Error.place(x=230, y=576)
            self.ML_Pass = False
            return

        self.RestingBP_Error.destroy()
        self.RestingBP_Error = customtkinter.CTkLabel(self.Background_Frame)
        RestingBP = float(RestingBP_Var)
        return RestingBP

    def prepare_Cholesterol(self):

        Cholesterol_Var = self.Cholesterol_Entry.get()

        if (Cholesterol_Var == '') or ((Cholesterol_Var.isnumeric() != True) and (isfloat(Cholesterol_Var) != True)):
            self.Cholesterol_Error.destroy()
            self.Cholesterol_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif, text='Enter a numeric value!', 
                                                            bg_color='white', fg_color='white', width=0, height=0)
            self.Cholesterol_Error.place(x=690, y=103)
            self.ML_Pass = False
            return

        self.Cholesterol_Error.destroy()
        self.Cholesterol_Error = customtkinter.CTkLabel(self.Background_Frame)
        Cholesterol = float(Cholesterol_Var)
        return Cholesterol

    def prepare_FastingBS(self):

        FastingBS_Var = self.FastingBS_Entry.get()

        if (FastingBS_Var == '') or ((FastingBS_Var.isnumeric() != True) and (isfloat(FastingBS_Var) != True)):
            self.FastingBS_Error.destroy()
            self.FastingBS_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif, text='Enter a numeric value!', 
                                                          bg_color='white', fg_color='white', width=0, height=0)
            self.FastingBS_Error.place(x=690, y=161)
            self.ML_Pass = False
            return

        self.FastingBS_Error.destroy()
        self.FastingBS_Error = customtkinter.CTkLabel(self.Background_Frame)

        if float(FastingBS_Var) > 120:
            FastingBS = 1.0
        else:
            FastingBS = 0.0
        return FastingBS

    def prepare_RestingECG(self):

        Map_RestingECG = {
            'Normal': 3, 'Left Ventricular Hypertrophy': 2, 'ST-T Wave Abnormality': 1}

        RestingECG_Var2 = self.RestingECG_Var.get()
        RestingECG_Var2 = RestingECG_Var2.strip()

        if RestingECG_Var2 not in self.RestingECG_options:
            self.RestingECG_Error.destroy()
            self.RestingECG_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif, 
                                                           text='Enter a valid option!', bg_color='white', fg_color='white', width=0, height=0)
            self.RestingECG_Error.place(x=695, y=228)
            self.ML_Pass = False
            return

        self.RestingECG_Error.destroy()
        self.RestingECG_Error = customtkinter.CTkLabel(self.Background_Frame)
        RestingECG = Map_RestingECG[RestingECG_Var2]
        return RestingECG

    def prepare_ExerciseAngina(self):

        Map_ExerciseAngina = {'No': 0, 'Yes': 1}
        ExerciseAngina = float(
            Map_ExerciseAngina[self.ExerciseAngina_Var.get()])

        return ExerciseAngina

    def prepare_MaxHR(self):

        MaxHR_Var = self.MaxHR_Entry.get()

        if (MaxHR_Var == '') or ((MaxHR_Var.isnumeric() != True) and (isfloat(MaxHR_Var) != True)):
            self.MaxHR_Error.destroy()
            self.MaxHR_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif,
                                                      text='Enter a numeric value!', bg_color='white', fg_color='white', width=0, height=0)
            self.MaxHR_Error.place(x=690, y=354)
            self.ML_Pass = False
            return

        self.MaxHR_Error.destroy()
        self.MaxHR_Error = customtkinter.CTkLabel(self.Background_Frame)
        MaxHR = float(MaxHR_Var)
        return MaxHR

    def prepare_Oldpeak(self):

        Oldpeak_Var = self.Oldpeak_Entry.get()

        if (Oldpeak_Var == '') or ((Oldpeak_Var.isnumeric() != True) and (isfloat(Oldpeak_Var) != True)):
            self.Oldpeak_Error.destroy()
            self.Oldpeak_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif,
                                                        text='Enter a numeric value!', bg_color='white', fg_color='white', width=0, height=0)
            self.Oldpeak_Error.place(x=690, y=403)
            self.ML_Pass = False
            return

        self.Oldpeak_Error.destroy()
        self.Oldpeak_Error = customtkinter.CTkLabel(self.Background_Frame)
        Oldpeak = float(Oldpeak_Var)
        return Oldpeak

    def prepare_STSlope(self):

        Map_STSlope = {'Flat': 1, 'Upsloping': 3, 'Downsloping': 2}

        STSlope_Var2 = self.STSlope_Var.get()
        STSlope_Var2 = STSlope_Var2.strip()

        if (STSlope_Var2 != 'Flat') and (STSlope_Var2 != 'Upsloping') and (STSlope_Var2 != 'Downsloping'):
            self.STSlope_Error.destroy()
            self.STSlope_Error = customtkinter.CTkLabel(self.Background_Frame, text_color='#CF1318', font=self.Noto_Serif,
                                                        text='Enter a valid option!', bg_color='white', fg_color='white', width=0, height=0)
            self.STSlope_Error.place(x=695, y=453)
            self.ML_Pass = False
            return

        self.STSlope_Error.destroy()
        self.STSlope_Error = customtkinter.CTkLabel(self.Background_Frame)
        STSlope = float(Map_STSlope[STSlope_Var2])
        return STSlope

    def predict(self):

        self.ML_Pass = True

        Sex = self.prepare_Sex()
        Age = self.prepare_Age()
        ChestPainType = self.prepare_ChestPainType()
        RestingBP = self.prepare_RestingBP()
        Cholesterol = self.prepare_Cholesterol()
        FastingBS = self.prepare_FastingBS()
        RestingECG = self.prepare_RestingECG()
        ExerciseAngina = self.prepare_ExerciseAngina()
        MaxHR = self.prepare_MaxHR()
        Oldpeak = self.prepare_Oldpeak()
        STSlope = self.prepare_STSlope()

        if self.ML_Pass == False:
            return

        self.Input.loc['Age'] = Age
        self.Input.loc['Sex'] = Sex
        self.Input.loc['ChestPainType'] = ChestPainType
        self.Input.loc['RestingBP'] = RestingBP
        self.Input.loc['Cholesterol'] = Cholesterol
        self.Input.loc['FastingBS'] = FastingBS
        self.Input.loc['RestingECG'] = RestingECG
        self.Input.loc['MaxHR'] = MaxHR
        self.Input.loc['ExerciseAngina'] = ExerciseAngina
        self.Input.loc['Oldpeak'] = Oldpeak
        self.Input.loc['ST_Slope'] = STSlope

        self.Storage.loc[10] = self.Input

        Probability_HD = (self.model.predict_proba(self.Storage).reshape([4,])[1])*100

        Result = customtkinter.CTkToplevel(fg_color='#FFF5F9')
        Result.transient(self)
        Result.geometry("600x325")
        Result.title('The Prediction')
        Result.iconbitmap(bitmap='icon.ico')

        Result_Frame = customtkinter.CTkFrame(Result, fg_color='#FFFFFF', width=600, height=325)
        Result_Frame.place(x=0, y=0)

        if Probability_HD >= 40:
            Result_Background = customtkinter.CTkImage(light_image=Image.open('Risk.png'), dark_image=Image.open('Risk.png'), size=(600, 325))
            Result_Background_Label = customtkinter.CTkLabel(Result_Frame, image=Result_Background, text='')
        else:
            Result_Background = customtkinter.CTkImage(light_image=Image.open('Not_Risk.png'), dark_image=Image.open('Not_Risk.png'), size=(600, 325))
            Result_Background_Label = customtkinter.CTkLabel(Result_Frame, image=Result_Background, text='')

        Result_Background_Label.place(x=0, y=0)

        Probability = customtkinter.CTkLabel(Result_Frame, text='The model calculates a ' + str(format(
            Probability_HD, '.1f')) + '% chance of cardiovascular disease.', text_color='#0C1765', font=self.Aileron, compound='center')
        Probability.place(x=74, y=96)

        Accuracy = customtkinter.CTkLabel(Result_Frame, text='(This model has a 90% accuracy in identifying risk of heart disease)',
                                          text_color='#0C1765', font=('Aileron', 15), compound='center')
        Accuracy.place(x=79, y=189)

        Ok_button = customtkinter.CTkButton(Result, text='Ok', bg_color='#FFF5F9', fg_color='#0C1765',
                                            font=self.Gotham, height=40, width=90, corner_radius=17, command=Result.destroy, hover_color='#505FC8')
        Ok_button.place(x=255, y=262)

    def clear(self):

        self.Age_Error.destroy()
        self.ChestPainType_Error.destroy()
        self.RestingBP_Error.destroy()
        self.Cholesterol_Error.destroy()
        self.FastingBS_Error.destroy()
        self.MaxHR_Error.destroy()
        self.Oldpeak_Error.destroy()
        self.RestingECG_Error.destroy()
        self.STSlope_Error.destroy()

        self.Age_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.ChestPainType_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.RestingBP_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.Cholesterol_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.FastingBS_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.MaxHR_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.Oldpeak_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.RestingECG_Error = customtkinter.CTkLabel(self.Background_Frame)
        self.STSlope_Error = customtkinter.CTkLabel(self.Background_Frame)

        self.Sex_Var.set('Male')
        self.Age_Entry.delete(0, customtkinter.END)
        self.Age_Entry._activate_placeholder()
        self.ChestPainType_Var.set('Asymptomatic')
        self.RestingBP_Entry.delete(0, customtkinter.END)
        self.RestingBP_Entry._activate_placeholder()
        self.Cholesterol_Entry.delete(0, customtkinter.END)
        self.Cholesterol_Entry._activate_placeholder()
        self.FastingBS_Entry.delete(0, customtkinter.END)
        self.FastingBS_Entry._activate_placeholder()
        self.RestingECG_Var.set('Normal')
        self.ExerciseAngina_Var.set('Yes')
        self.MaxHR_Entry.delete(0, customtkinter.END)
        self.MaxHR_Entry._activate_placeholder()
        self.Oldpeak_Entry.delete(0, customtkinter.END)
        self.STSlope_Var.set('Flat')

    def place_button(self):

        self.Graph_Image = customtkinter.CTkImage(light_image=Image.open('Graph_Final_2.png'), dark_image=Image.open('Graph_Final_2.png'), size=(42, 19))
        self.Predict_button = customtkinter.CTkButton(self.Background_Frame, command=self.predict, width=180, height=66, text=' Predict',
                                                      bg_color='#FFF5F9', fg_color='#0C1765', corner_radius=25, image=self.Graph_Image, font=self.Gotham, compound='left', hover_color='#505FC8')
        self.Predict_button.place(x=479, y=568)

        self.Eraser_Image = customtkinter.CTkImage(light_image=Image.open('Eraser_Final_2.png'), dark_image=Image.open('Eraser_Final_2.png'), size=(29, 25))
        self.Clear_button = customtkinter.CTkButton(self.Background_Frame, text='  Clear', command=self.clear, width=180, height=66, bg_color='#FFF5F9',
                                                    fg_color='#0C1765', corner_radius=25, font=self.Gotham, compound='left', image=self.Eraser_Image, hover_color='#505FC8')
        self.Clear_button.place(x=690, y=568)


def main():

    HDP = HeartDiseasePrediction()
    HDP.mainloop()


if __name__ == '__main__':
    main()

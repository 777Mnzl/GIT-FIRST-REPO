import pywhatkit as p
txt = ''' Moomin, the beloved 1990s show, captured the hearts of audiences with its enchanting tales and whimsical characters. Based on the Swedish-Finnish comic strip by Tove Jansson, the animated series transported viewers to the magical world of Moominvalley. The show followed the adventures of the Moomin family, led by Moominmamma and Moominpappa, alongside their curious and kind-hearted son, Moomintroll. 
Together with their friends, such as Snufkin, Snork Maiden, and Little My, they embarked on imaginative journeys, encountering fantastical creatures and overcoming various challenges. Moomin exuded a timeless charm, blending gentle life lessons with a sense of wonder, making it a treasured show that continues to captivate audiences to this day.'''

p.text_to_handwriting(txt, 'demo1.png', [0, 0, 138])
print('END')

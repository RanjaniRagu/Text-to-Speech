import pyttsx3
# Reference text
reference_text = input("Enter the reference text for finding accuracy:")
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Set properties (optional)
engine.setProperty('rate', 150) # Speed of speech
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)
# Text to be converted to speech
text = input("Enter the text to convert:")
# Convert the text to speech
engine.say(text)
# Play the speech
engine.runAndWait()
# Calculate accuracy
def calculate_accuracy(reference, generated):
 # Assuming both texts are of same length
 if len(reference) != len(generated):
 return 0.0
 correct_chars = sum(1 for r, g in zip(reference, generated) if r == g)
 total_chars = len(reference)
 accuracy = correct_chars / total_chars * 100
 return accuracy
# Calculate accuracy of generated speech
accuracy = calculate_accuracy(reference_text, text)
print("Accuracy:", accuracy, "%")

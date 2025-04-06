import morse_python as mp

# Testare la funzione morse_to_text
morse_code = ".--. .-. .. -. - -.--. .-..-. .... .. .-..-. -.--.-"
print("Morse to Text:", mp.morse_to_text(morse_code))

# Testare la funzione text_to_morse
python_code = 'print("Hello, World!")'
print("Text to Morse:", mp.text_to_morse(python_code))

# Testare la funzione execute_morse_code
morse_code_for_execution = ".--. .-. .. -. - -.--. .-..-. .... .. .-..-. -.--.-"
print("Execute Morse Code output:")
mp.execute_morse_code(morse_code_for_execution)
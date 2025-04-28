# Email polite rephraser

This project demonstrates a **local application** using a **large language model** (LLM) to rephrase blunt or harsh sentences into polite, professional email responses. The app runs fully offline using the llama3.2:3b model via the Ollama runtime, specially focuses on hallucination control, and provides a graphical user interface for input and output. 

## Model Used: llama3.2:3b
A small, instruction-following language model ideal for rephrasing, summarizing, and other short tasks. It is fast, lightweight, and works well for local apps without requiring a GPU. In this project it specially uses to rephrase blunt sentences into polite one.

Notice: Ollama, the platform providing the model, is licensed separately. See [Ollama's official website](https://ollama.com/library/llama3.2) for details.

![llama](https://github.com/user-attachments/assets/66f8f12e-3b9b-4931-87b9-2c3cd440633a)


## Code Function Explane
The application is written in Python using Tkinter for the GUI and subprocess to connect with the local LLM through Ollama. The make_polite() function handles prompt formatting, calls the LLM, and filters the output. It ensures only the useful polite response is returned.

The run_rephraser() function connects the GUI with the model. It fetches the user's input, sends it to make_polite() and displays the result in the GUI.

Styling of the GUI is handled with font and color constants such as FONT_LARGE, ACCENT, and CARD_BG, giving the application a modern card-style layout.

## Hallucination Control
To prevent hallucination and keep responses focused, I experimented with adding examples in the **system prompt** but found that this sometimes caused the model to generate unrelated or overexplain. Based on that, I removed the examples and now rely on a concise instruction-only prompt, which gives clear direction without interfering with the model’s natural rephrasing ability. Additionally, I applied output filtering to strip away unnecessary phrases like apologies or polite closings, ensuring that only the necessary output is returned.

## Results
Below is a sample of the running application.

![result1](https://github.com/user-attachments/assets/777bd09c-3910-4d0d-abc9-23e45ca3028a)
![result2](https://github.com/user-attachments/assets/f0ea52ff-0b09-47fb-9525-4f5179dd6035)



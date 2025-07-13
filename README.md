# Customer Support Chatbot (Fine-Tuned DialoGPT)

A fine-tuned conversational AI chatbot designed to handle customer support queries using Microsoft's DialoGPT model. This project adapts a general-purpose language model to a customer service context using a real-world dataset of ~27,000 instruction-response pairs.

> 🔗 **Kaggle Model**: [Dialogpt-Fine-TunedCustomer-Service](https://www.kaggle.com/models/suyashkb/dialogpt-fine-tunedcustomer-service)

---

## Project Highlights

- Fine-tuned on real-world customer support data.
- Built on top of [`microsoft/DialoGPT-medium`](https://huggingface.co/microsoft/DialoGPT-medium).
- Trained using the [Bitext Customer Support Dataset](https://www.kaggle.com/datasets/bitext/customer-support-dataset).
- Quantized to FP8 precision for easy local deployment and faster inference time. 
- Deployed with an easy-to-use **Streamlit interface**.
- Fully local and offline-ready inference pipeline.
- Modular and readable code structure.

---

## Dataset

- **Name**: Bitext Sample Customer Support Dataset
- **Size**: 27,000 instruction-response pairs
- **Format**: CSV with `instruction` and `response` columns
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/bitext/customer-support-dataset)

---

## Model Architecture

- **Base Model**: [`DialoGPT-medium`](https://huggingface.co/microsoft/DialoGPT-medium)
- **Tokenizer**: AutoTokenizer with EOS token as padding
- **Training Framework**: Hugging Face Transformers
- **Loss**: Causal LM Loss using language modeling head
- **Batch Size**: 2
- **Epochs**: 3

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/customer-support-chatbot.git
cd customer-support-chatbot
```

### 2. Install Dependencies
```bash 
pip install -r requirements.txt
```

### 3. Download and place the model files ###
Download the model.zip file and place it in the same directory as the chatbot 

### 4. Run the chatbot locally
`streamlit run app.py`

## Example Usage
**User:** "Hi,how do I reset my password?"
**Bot:** "Sure! ou can reset your password by clicking on 'Forget Password' at the login screen.
Follow the steps sent to your registered email."

## Future Work
- Soon to be implemented Retreival Augmented Generation (RAG) for easy customization
- Add support for multi-turn conversations
- Deploy using Gradio or Hugging face spaces
- Integrate feedback loop for real-time improvement
- Extend support for multilingual queries.
  

from nltk import ngrams
from transformers import BertTokenizer, BertModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from gensim.models import Word2Vec

# Function to generate n-grams
def generate_ngrams(sentence, n):
    # Tokenize the sentence into words
    words = sentence.split()
    # Generate n-grams
    n_grams = list(ngrams(words, n))
    return n_grams

def creating_planets(sentence,ngram_sizes,pull):
    # Load the pre-trained BERT model and tokenizer
    model_name = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name, output_attentions=True)

    # Tokenize the sentence
    inputs = tokenizer(sentence, return_tensors="pt")

    # Get the model outputs (including attention weights)
    outputs = model(**inputs)

    # Extract attention weights
    attentions = outputs.attentions

    # Select the last layer for visualization
    last_layer_attention = attentions[-1]

    # Average over all attention heads
    attention_matrix = last_layer_attention[0].mean(dim=0).detach().numpy()

    # Get the tokenized words
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # Generate a list of tokens and their attention values
    attention_list = []
    for i, token in enumerate(tokens):
        focus = {tokens[j]: attention_matrix[i][j] for j in range(len(tokens))}
        attention_list.append({token: focus})
    
    attention_ngram = []
    # Process n-grams and identify the ones with higher attention
    for n in ngram_sizes:
        n_grams = generate_ngrams(sentence, n)
        for ngram in n_grams:
            # Calculate average attention for the n-gram
            avg_attention = sum(
                [attention_matrix[tokens.index(token), tokens.index(token)] for token in ngram if token in tokens]
            ) / len(ngram)
            if avg_attention > pull:
                # Output the n-gram and its attention score
                attention_ngram.append(ngram)
    return attention_ngram

def planet_lm(attention_ngram, max_length, depth):
    # Flatten the list of n-grams into a list of words
    words = set([word for ngram in attention_ngram for word in ngram])

    # Step 1: Train Word2Vec
    w2v_model = Word2Vec(sentences=[list(words)], vector_size=50, min_count=1, workers=4)

    # Step 2: Use Word2Vec to find similar words
    similar_words = {}
    for word in words:
        similar_words[word] = [w for w, _ in w2v_model.wv.most_similar(word, topn=5)]

    # Step 3: Prepare GPT-2 for sentence generation
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Generate new sentences using GPT-2 and build a paragraph
    generated_paragraph = ""
    word_count = 0
    sentence_in_progress = ""

    while word_count < 100:
        for word, sims in similar_words.items():
            input_text = f"{word} {' '.join(sims)}"
            input_ids = tokenizer.encode(input_text, return_tensors="pt")
            output = model.generate(input_ids, max_length=max_length // depth, num_return_sequences=1, do_sample=True)
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

            # Add the generated text to the sentence in progress
            sentence_in_progress += " " + generated_text

            # Split the sentence into words
            words_in_sentence = sentence_in_progress.split()

            # Add words to the paragraph until we reach the limit
            for w in words_in_sentence:
                if word_count >= 100 and w.endswith(('.')):
                    # Complete the sentence if the word limit is exceeded
                    generated_paragraph += " " + sentence_in_progress.strip()
                    return generated_paragraph.strip()

                if word_count < 100:
                    generated_paragraph += " " + w
                    word_count += 1
                else:
                    # If the limit is reached but the sentence isn't complete, continue.
                    continue

            # Reset the sentence in progress
            sentence_in_progress = ""

    # Return the paragraph (in case the loop ends naturally)
    return generated_paragraph.strip()

def llm_genUniverse(sentence, ngram_sizes, depth, pull, max_length):
    output = ""
    depth = depth + 1
    for _ in range(depth-1):
        sentence = sentence
        attention_ngram = creating_planets(sentence,ngram_sizes,pull)
        planet_lm_output = planet_lm(attention_ngram,max_length,depth)
        depth = depth - 1
        sentence = planet_lm_output[1:-1]
        output += planet_lm_output[1:-1]
    print(output)

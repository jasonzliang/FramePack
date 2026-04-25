import os


def login(token, max_retries=5):
    from huggingface_hub import login
    import time

    for attempt in range(max_retries):
        try:
            login(token)
            print('HF login ok.')
            return
        except Exception as e:
            print(f'HF login failed (attempt {attempt + 1}/{max_retries}): {e}')
            if attempt < max_retries - 1:
                time.sleep(0.5)
    print('HF login failed after all retries. Continuing without login.')


hf_token = os.environ.get('HF_TOKEN', None)

if hf_token is not None:
    login(hf_token)

from nemo_text_processing.text_normalization.normalize import Normalizer
normalizer = Normalizer(input_case='cased', lang='en')



written = "We paid $123 for this desk."
normalized = normalizer.normalize(written, verbose=True, punct_post_process=True)
print(normalized)


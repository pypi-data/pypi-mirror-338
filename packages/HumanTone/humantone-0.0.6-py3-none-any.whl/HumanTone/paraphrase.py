try:
    from parrot import Parrot

    parrot = Parrot()

    def paraphrase_text(text: str) -> str:
        paraphrases = parrot.augment(input_phrase=text)
        return paraphrases[0] if paraphrases else text

except ImportError:
    def paraphrase_text(text: str) -> str:
        return ("Parrot module not installed. Please install it using: "
                "`pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git`")

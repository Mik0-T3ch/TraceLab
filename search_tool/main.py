from core.detector import detect_type
from core.normalizer import normalize
from core.generator import generate
from services.file_writer import save


def main():
    value = input("Ingresa un dato: ")

    tipo = detect_type(value)
    variants = normalize(value, tipo)
    dorks = generate(variants)

    save(value, dorks)


if __name__ == "__main__":
    main()
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.modelo import prever_preco

def test_preco_valido():
    assert prever_preco(3000, 50) == 3000 * 0.3 + 50 * 1500

def test_preco_invalido():
    assert prever_preco(0, 50) == 0
    assert prever_preco(3000, 0) == 0

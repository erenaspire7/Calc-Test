import calculator

def test_calc():
    input_values = [2,3]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    calculator.input = mock_input
    calculator.print = lambda s : output.append(s)

    calculator.main()

    assert output == [
        'Enter number 1: ',
        'Enter number 2: ',
        'The result is 6'
    ] 
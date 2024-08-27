from django.shortcuts import render

def calculator_view(request):
    context = {
        'number1': '',
        'number2': '',
        'operation': '',
        'result': None
    }
    
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')
        
        try:
            number1 = float(number1)
            number2 = float(number2)
        except ValueError:
            context['result'] = 'Error: Introduzca valores numéricos válidos.'
            context['number1'] = number1
            context['number2'] = number2
            context['operation'] = operation
            return render(request, 'calculator.html', context)

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 != 0:
                result = number1 / number2
            else:
                result = 'Error: División por cero.'
        else:
            result = 'Error: Operación no válida.'

        context['result'] = result
        context['number1'] = number1
        context['number2'] = number2
        context['operation'] = operation
    
    return render(request, 'calculator.html', context)
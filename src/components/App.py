from snakeskin.framework import Component
class App(Component):
    def render(self):
        return """
        <section class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 class="text-4xl font-bold text-blue-600">Welcome to Snakeskin!</h1>
            <p class="mt-4 text-lg text-gray-700">Your modern Python framework.</p>
        </section>
        """ 

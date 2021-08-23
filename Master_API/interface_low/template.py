class template_interface_low:

    def __init__(self):
        """
        vous pouvez en ajouter au besoin
        """

    def start(self):
        """
        permet de faire des initialisation de votre coté, test de connection ....
        """
        pass

    def destroy(self):
        """
        potentiellement vide, avec de la suppression d'infomation si vous créer des object le nécissitant.
        """
        pass

    def featuresloop(self):
        """
        la boucle infinie de la features est ici
        """
        while self.__running is True:
            """
            logique de la fonction
            """
            break

    def activate(self):
        """
        activer la features
        """
        self.__running = True

    def desactivate(self):
        """
        desacative la features
        """
        self.__running = False

import numpy as np
import random

class State:
    def __init__(self, size=3):
        self.size = size
        self.faces = np.zeros((6, size, size), dtype=int)
        
        for k in range(6):
            self.faces[k, :, :] = k

        #print(self.faces)

    def front_clock(self):

        temp = self.faces[2, 2, :].copy()  # Superior traseira
        self.faces[2, 2, :] = self.faces[4, :, 0][::-1]  # Superior <- Esquerda (invertida)
        self.faces[4, :, 0] = self.faces[3, 0, :][::-1]  # Esquerda <- Inferior (invertida)
        self.faces[3, 0, :] = self.faces[5, :, 0][::-1]  # Inferior <- Direita (invertida)
        self.faces[5, :, 0] = temp  # Direita <- Superior
        #face_copy = self.faces[1].copy()
        
        
        self.faces[1] = np.rot90(self.faces[1], k=-1)
        
        # for i in range(self.size):
        #     for j in range(self.size):
        #         self.faces[1, i, j] = face_copy[self.size-1-j, i]

    def front_anticlock(self):
        temp = self.faces[2, 2, :].copy()  # Superior traseira
        self.faces[2, 2, :] = self.faces[5, :, 0]  # Superior <- Direita
        self.faces[5, :, 0] = self.faces[3, 0, :][::-1]  # Direita <- Inferior (invertida)
        self.faces[3, 0, :] = self.faces[4, :, 0][::-1]  # Inferior <- Esquerda (invertida)
        self.faces[4, :, 0] = temp[::-1]  # Esquerda <- Superior (invertida)
        #face_copy = self.faces[1].copy()
        
        self.faces[1] = np.rot90(self.faces[1], k=1)
        
        # for i in range(self.size):
        #     for j in range(self.size):
        #         self.faces[1, i, j] = face_copy[j, self.size-1-i]

    def back_clock(self):
        temp = self.faces[2, 2, :].copy()  # Superior traseira
        self.faces[2, 2, :] = self.faces[4, :, 0][::-1]  # Superior <- Esquerda (invertida)
        self.faces[4, :, 0] = self.faces[3, 0, :][::-1]  # Esquerda <- Inferior (invertida)
        self.faces[3, 0, :] = self.faces[5, :, 0][::-1]  # Inferior <- Direita (invertida)
        self.faces[5, :, 0] = temp  # Direita <- Superior
        # face_copy = self.faces[1].copy()
        
        self.faces[1] = np.rot90(self.faces[1], k=-1)
        
        # for i in range(self.size):
        #     for j in range(self.size):
        #         self.faces[1, i, j] = face_copy[self.size-1-j, i]

    def back_anticlock(self):
        temp = self.faces[2, 2, :].copy()  # Superior traseira
        self.faces[2, 2, :] = self.faces[5, :, 0]  # Superior <- Direita
        self.faces[5, :, 0] = self.faces[3, 0, :][::-1]  # Direita <- Inferior (invertida)
        self.faces[3, 0, :] = self.faces[4, :, 0][::-1]  # Inferior <- Esquerda (invertida)
        self.faces[4, :, 0] = temp[::-1]  # Esquerda <- Superior (invertida)
        face_copy = self.faces[1].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[1, i, j] = face_copy[j, self.size-1-i]
   
    # esta rotacionando a parte superior ao contrario
    # rotacoes laterais erradas
    def up_clock(self):
      temp = self.faces[0, 0, :].copy()  # Salva a linha superior da face da frente
      self.faces[0, 0, :] = self.faces[5, 0, ::-1]  # Frente recebe Direita (invertida)
      self.faces[5, 0, :] = self.faces[1, 0, ::-1]  # Direita recebe Traseira (invertida)
      self.faces[1, 0, :] = self.faces[4, 0, ::-1]  # Traseira recebe Esquerda (invertida)
      self.faces[4, 0, :] = temp[::-1]  # Esquerda recebe Frente (invertida)

      face_copy = self.faces[3].copy()
      for i in range(self.size):
          for j in range(self.size):
              self.faces[3, i, j] = face_copy[self.size - 1 - j, i]

    # esta rotacionando a parte superior ao contrario
    def up_anticlock(self):
      temp = self.faces[0, 0, :].copy()  # Salva a linha superior da face da frente
      self.faces[0, 0, :] = self.faces[4, 0, ::-1]  # Frente recebe Esquerda (invertida)
      self.faces[4, 0, :] = self.faces[1, 0, ::-1]  # Esquerda recebe Traseira (invertida)
      self.faces[1, 0, :] = self.faces[5, 0, ::-1]  # Traseira recebe Direita (invertida)
      self.faces[5, 0, :] = temp[::-1]  # Direita recebe Frente (invertida)

      face_copy = self.faces[3].copy()
      for i in range(self.size):
          for j in range(self.size):
              self.faces[3, i, j] = face_copy[j, self.size - 1 - i]


    def down_clock(self):
      temp = self.faces[0, 2, :].copy()  # Frente inferior
      self.faces[0, 2, :] = self.faces[4, 2, :]  # Frente <- Esquerda
      self.faces[4, 2, :] = self.faces[1, 2, :]  # Esquerda <- Traseira
      self.faces[1, 2, :] = self.faces[5, 2, :]  # Traseira <- Direita
      self.faces[5, 2, :] = temp  # Direita <- Frente
      face_copy = self.faces[2].copy()
      for i in range(self.size):
          for j in range(self.size):
              self.faces[2, i, j] = face_copy[self.size-1-j, i]

    def down_anticlock(self):
        temp = self.faces[0, 2, :].copy()  # Frente inferior
        self.faces[0, 2, :] = self.faces[5, 2, :]  # Frente <- Direita
        self.faces[5, 2, :] = self.faces[1, 2, :]  # Direita <- Traseira
        self.faces[1, 2, :] = self.faces[4, 2, :]  # Traseira <- Esquerda
        self.faces[4, 2, :] = temp  # Esquerda <- Frente
        face_copy = self.faces[2].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[2, i, j] = face_copy[j, self.size-1-i]

    def left_clock(self):
        temp = self.faces[0, :, 0].copy()  # Frente esquerda
        self.faces[0, :, 0] = self.faces[2, :, 0]  # Frente <- Superior
        self.faces[2, :, 0] = self.faces[1, :, 2][::-1]  # Superior <- Traseira (invertida)
        self.faces[1, :, 2] = self.faces[3, :, 0][::-1]  # Traseira <- Inferior (invertida)
        self.faces[3, :, 0] = temp  # Inferior <- Frente
        face_copy = self.faces[4].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[4, i, j] = face_copy[self.size-1-j, i]

    def left_anticlock(self):
        temp = self.faces[0, :, 0].copy()  # Frente esquerda
        self.faces[0, :, 0] = self.faces[3, :, 0]  # Frente <- Inferior
        self.faces[3, :, 0] = self.faces[1, :, 2][::-1]  # Inferior <- Traseira (invertida)
        self.faces[1, :, 2] = self.faces[2, :, 0][::-1]  # Traseira <- Superior (invertida)
        self.faces[2, :, 0] = temp  # Superior <- Frente
        face_copy = self.faces[4].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[4, i, j] = face_copy[j, self.size-1-i]

    def right_clock(self):
        temp = self.faces[0, :, 2].copy()  # Frente direita
        self.faces[0, :, 2] = self.faces[3, :, 2]  # Frente <- Inferior
        self.faces[3, :, 2] = self.faces[1, :, 0][::-1]  # Inferior <- Traseira (invertida)
        self.faces[1, :, 0] = self.faces[2, :, 2][::-1]  # Traseira <- Superior (invertida)
        self.faces[2, :, 2] = temp  # Superior <- Frente
        face_copy = self.faces[5].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[5, i, j] = face_copy[self.size-1-j, i]

    def right_anticlock(self):
        temp = self.faces[0, :, 2].copy()  # Frente direita
        self.faces[0, :, 2] = self.faces[2, :, 2]  # Frente <- Superior
        self.faces[2, :, 2] = self.faces[1, :, 0][::-1]  # Superior <- Traseira (invertida)
        self.faces[1, :, 0] = self.faces[3, :, 2][::-1]  # Traseira <- Inferior (invertida)
        self.faces[3, :, 2] = temp  # Inferior <- Frente
        face_copy = self.faces[5].copy()
        for i in range(self.size):
            for j in range(self.size):
                self.faces[5, i, j] = face_copy[j, self.size-1-i]

    
import csv
from datetime import datetime
import os
import face_recognition
import cv2
import numpy as np

class ReconhecimentoFacial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.registros_faciais = {}
        return cls._instance
    
    def criar_relacao_foto_matricula(self, alunos):
        known_face_encodings = []
        known_face_matricula = []  
        for aluno in alunos:
            load_Image = face_recognition.load_image_file(aluno[3])
            image_face_encoding = face_recognition.face_encodings(load_Image)[0]
            known_face_encodings.append(image_face_encoding)         
            known_face_matricula.append(aluno[1])
        return [known_face_encodings,known_face_matricula]


    # def reconhecimento_facial(self, alunos, video=None):
    #     video_capture = cv2.VideoCapture(0)
    #     alunos_presentes = []
    #     id_cadeira = alunos[0][2]
    #     known_face_encodings, known_face_matricula = self.criar_relacao_foto_matricula(alunos)[0], self.criar_relacao_foto_matricula(alunos)[1]

    #     process_this_frame = True

    #     while True:
    #         ret, frame = video_capture.read()

    #         if process_this_frame:
    #             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #             rgb_small_frame = small_frame[:, :, ::-1]

    #             face_locations = face_recognition.face_locations(rgb_small_frame)
    #             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    #             face_matricula = []

    #             for face_encoding in face_encodings:
    #                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    #                 matricula = "Unknown"

    #                 face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    #                 best_match_index = np.argmin(face_distances)
    #                 if matches[best_match_index]:
    #                     matricula = known_face_matricula[best_match_index]
    #                     if matricula not in alunos_presentes:
    #                         alunos_presentes.append(matricula)

    #                 face_matricula.append(matricula)

    #         # Atualizar a variável process_this_frame
    #         process_this_frame = not process_this_frame

    #         # Exibir a imagem com as marcações
    #         cv2.imshow('Video', frame)

    #         # Verificar se o processo está completo
    #         # Verificar se o usuário pressionou a tecla "Q"
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break

    #     # Encerrar a captura de vídeo
    #     video_capture.release()
    #     cv2.destroyAllWindows()

    #     # Verificar alunos faltantes
    #     alunos_faltantes = [aluno[1] for aluno in alunos if aluno[1] not in alunos_presentes]

    #     # Nome da pasta para salvar o arquivo CSV
    #     nome_pasta = 'csv'
    #     # Verificar se a pasta existe, caso contrário, criá-la
    #     if not os.path.exists(nome_pasta):
    #         os.makedirs(nome_pasta)

    #     # Gerar nome do arquivo com base no ID da cadeira e na data atual
    #     data_atual = datetime.now().strftime("%Y-%m-%d")
    #     nome_arquivo = f"{id_cadeira}_{data_atual}.csv"

    #     # Caminho completo para o arquivo
    #     caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

    #     # Gerar arquivo CSV
    #     with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
    #         writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #         writer.writerow(['Nome do aluno', 'Matrícula', 'Presença'])
    #         for aluno in alunos:
    #             nome = aluno[0]
    #             matricula = aluno[1]
    #             presenca = 'Presente' if matricula in alunos_presentes else 'Faltante'
    #             writer.writerow([nome, matricula, presenca])
    #     return [alunos_presentes, alunos_faltantes, caminho_arquivo]
    
    
    def reconhecimento_facial(self, alunos, video=None):
        video_capture = cv2.VideoCapture(video)  # Abre o arquivo de vídeo

        alunos_presentes = []
        id_cadeira = alunos[0][2]
        known_face_encodings, known_face_matricula = self.criar_relacao_foto_matricula(alunos)[0], self.criar_relacao_foto_matricula(alunos)[1]

        process_this_frame = True

        while video_capture.isOpened():
            ret, frame = video_capture.read()

            if not ret:  # Se não foi possível ler o frame, encerra o loop
                break

            if process_this_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_matricula = []
                face_matches = []

                for face_encoding in face_encodings:
                    distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    min_distance_index = np.argmin(distances)
                    min_distance = distances[min_distance_index]

                    if min_distance <= 0.6:  # Ajuste o limite de distância para considerar como uma correspondência
                        matricula = known_face_matricula[min_distance_index]
                        if matricula not in face_matches:
                            face_matches.append(matricula)
                            face_matricula.append(matricula)
                            if matricula not in alunos_presentes:
                                alunos_presentes.append(matricula)
                    else:
                        face_matricula.append("Unknown")

            # Atualizar a variável process_this_frame
            process_this_frame = not process_this_frame

            # Verificar se o usuário pressionou a tecla "Q"
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Encerrar a captura de vídeo
        video_capture.release()
        cv2.destroyAllWindows()

        # Verificar alunos faltantes
        alunos_faltantes = [aluno[1] for aluno in alunos if aluno[1] not in alunos_presentes]

        # Nome da pasta para salvar o arquivo CSV
        nome_pasta = 'csv'
        # Verificar se a pasta existe, caso contrário, criá-la
        if not os.path.exists(nome_pasta):
            os.makedirs(nome_pasta)

        # Gerar nome do arquivo com base no ID da cadeira e na data atual
        data_atual = datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"{id_cadeira}_{data_atual}.csv"

        # Caminho completo para o arquivo
        caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

        # Gerar arquivo CSV
        with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nome do aluno', 'Matrícula', 'Presença'])
            for aluno in alunos:
                nome = aluno[0]
                matricula = aluno[1]
                presenca = 'Presente' if matricula in alunos_presentes else 'Faltante'
                writer.writerow([nome, matricula, presenca])

        return [alunos_presentes, alunos_faltantes, caminho_arquivo]


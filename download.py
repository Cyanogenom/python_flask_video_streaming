import requests

if __name__ == "__main__":
	url = 'http://127.0.0.1:5000/stream'
	part_size = 10000
	parts_dir = './parts'
	index = 0
	file_index = 0

	data = requests.get(url, stream=True)
	file = open('downloaded_file.mov', 'wb')
	part_file = open(f'{parts_dir}/part_{file_index}_file.mov', 'wb')
	for chunk in data.iter_content(chunk_size=1024):
		print(index)
		if index < part_size:
			if chunk:
				part_file.write(chunk)
			index += 1

		else:
			part_file.close()
			index = 0
			file_index += 1
			part_file = open(f'{parts_dir}/part_{file_index}_file.mov', 'wb')

		if chunk:
			file.write(chunk)
	part_file.close()
	file.close()
	print('saved')
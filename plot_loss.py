import matplotlib.pyplot as plt

def read_loss():
	f = open('loss', 'r')
	d_loss = []
	g_loss = []
	count = 0
	for line in f:
		if count % 2 == 0:
			loss = float(line)
			g_loss.append(loss)
		else:
			loss = float(line)
			d_loss.append(loss)
		count = count + 1
	return (d_loss, g_loss)
			
if __name__ == "__main__":
	d_loss, g_loss = read_loss()
	plt.figure(1)
	plt.subplot(211)
	plt.plot(d_loss)
	plt.ylabel('Discriminators loss')
	plt.xlabel('number of epochs')
	plt.subplot(212)
	plt.plot(g_loss)
	plt.ylabel('Generators loss')
	plt.xlabel('number of epochs')
	plt.show()
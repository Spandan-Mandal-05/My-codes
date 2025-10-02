import matplotlib.pyplot as plt 
import numpy as np 
plt.style.use('classic')


def collatz_sequence(n):
    sequence=[n]
    while n!=1:
        n=n//2 if n%2==0 else 3*n+1 
        sequence.append(n)
    return sequence

def collatz_length(n):
    return len(collatz_sequence(n))

n=500
m=9331


mm=collatz_sequence(m)
nn=[collatz_length(i) for i in range(5,n+1)]
steps, frequency = np.unique(nn, return_counts=True)

average_step = np.mean(nn)
most_appeared_step = steps[np.argmax(frequency)]
max_possible_step = np.max(nn)
least_possible_step = np.min(nn)
max_at=nn.index(max(nn))+5

collatz_sequences = []
for i in range(5, n+1):
    collatz_sequences.extend(collatz_sequence(i))
zz=np.vectorize(lambda s: int(str(s)[0]))(collatz_sequences)
terms, appearence=np.unique(zz,return_counts=True)

fig,ax=plt.subplots(2,2,figsize=(8,8))
props = dict(boxstyle='round', alpha=0.5)

ax[0][0].plot(mm)
ax[0][0].set_title(f'Collatz Sequence of {m}')
ax[0][0].set_xlabel('Step Number')
ax[0][0].set_ylabel('Sequence Value')
ax[0][0].axhline(y=0,linewidth=1,alpha=0.5)
ax[0][0].axvline(x=0,linewidth=1,alpha=0.5)
ax[0][0].text(0.73, 0.98, f'Max={max(mm)}', 
              transform=ax[0][0].transAxes, fontsize=10,
        verticalalignment='top', bbox=props, ha='left')

ax[0][1].hist(np.arange(5,n+1),weights=nn, bins=range(5,n+2))
ax[0][1].set_title('Length of Collatz Sequences')
ax[0][1].set_xlabel('Seed Number')
ax[0][1].set_ylabel('Sequence Length')

ax[1][0].hist(steps, weights=frequency, bins=range(1, max(nn) + 1))
textstr = '\n'.join((
    f'Average: {average_step:.2f}',
    f'Most Common: {most_appeared_step}',
    f'Max : {max_possible_step}',
    f'Min: {least_possible_step}',
    f'Max at: {max_at}'))

ax[1][0].text(0.45, 0.95, textstr, transform=ax[1][0].transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax[1][0].set_title('Frequency of Steps in Collatz Sequences')
ax[1][0].set_xlabel('Number of Steps')
ax[1][0].set_ylabel('Frequency')

ax[1][1].hist(terms,weights=appearence,bins=range(1, max(zz) + 2),edgecolor='black')
ax[1][1].set_title("Benford's Law Verification")
ax[1][1].set_xlabel('First Digit')
ax[1][1].set_ylabel('Frequency')
plt.tight_layout()
plt.show()
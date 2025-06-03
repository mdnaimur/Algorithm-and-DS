from LinkedListQ.PlayerLinkedQ import PlayerLinkedQueue
from PlayerMatch import PlayerMatch


print("\n Arraybased Queue\n")
pm = PlayerMatch(3)
pm.joinQueue('Mamun')
pm.joinQueue("Naimur")


pm.joinQueue("Kawsar")
pm.joinQueue("Sumon")
pm.joinQueue("Parvez")

print("*" * 30)
print("\nLinkedList Queue\n")
print("*" * 30)

lq = PlayerLinkedQueue()
lq.joinPlayer('Bangladesh')
lq.joinPlayer("Pakistan")


lq.joinPlayer("India")
lq.joinPlayer("Srilanka")
lq.joinPlayer("Nepal")
lq.joinPlayer("Austrilia")
lq.joinPlayer("England")

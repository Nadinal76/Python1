from address import Address
from mailing import Mailing

to_adr = Address("190000", "Санкт-Петербург", "Невский проспект", "10", "25")
from_adr = Address("672024", "Чита", "Казачья улица", "5", "12")

mail = Mailing(to_address=to_adr, from_address=from_adr, cost=450, track="TRACK123456")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")

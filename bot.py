import discord 
from discord.ext import commands

PREFIX = '!'

client = commands.Bot(command_prefix = PREFIX)
client.remove_command( 'help' )

#WOrds
hello_words = [ 'hello', 'hi', 'привет', 'privet', 'ky','ку','дарова','здарова' ]
answer_words = ['узнать информацию о сервере', 'что здесь есть', 'команды', 'команды сервера', 'что здесь делать',]
goodbye_words = ['bb', 'poka', 'goodbye', 'bb all', 'всем пока', 'досвидос', 'бб', 'пока', 'до завтра']

@client.event

#запуск
async def on_ready ():
	print('BOT connected' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game('Bruh') )
@client.event

#чат-бот
async def on_message ( message ):
	msg = message.content.lower()
	await client.process_commands( message )

	if msg in hello_words: 
		await message.channel.send( 'и тебе привет' )
	if msg in answer_words: 
		await message.channel.send( 'Напиши в чат !help и узнаешь' )
	if msg in goodbye_words: 
		await message.channel.send( 'Увидимся завтра!' )


#role
@client.event 

async def on_member_join( member ):
	channel = client.get_channel( 681032641545633829 )

	role = discord.utils.get( member.guild.roles, id = 681145622723952708)

	await member.add_roles( role )
	await channel.send( embed = discord.Embed( description = f'Пользователь ``{member.name}``, присоеденился к нам!', color = 0x0c0c0c  ) )

#clear		
@client.command()
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 100 ):
  await ctx.channel.purge(limit = amount)

#clear messages  
@client.command()
async def hello( ctx, amount = 1):
  await ctx.channel.purge(limit = amount)

  author = ctx.message.author
  await ctx.send(f'Hello { author.mention }' )

#Kick
@client.command()  
@commands.has_permissions( administrator = True )

async def kick(ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1)

	await member.kick( reason = reason)
	await ctx.send(f'kick user {member.mention}')

#Ban
@client.command()  
@commands.has_permissions( administrator = True )

async def ban(ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1)

	await member.ban( reason = reason)
	await ctx.send(f'ban user {member.mention}')

#Unban
@client.command()  
@commands.has_permissions( administrator = True )

async def unban( ctx, *, member, ):
	await ctx.channel.purge( limit = 1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban( user )
		await ctx.send(f'Unbanned user {user.mention}')

		return

#help
@client.command()  

async def help( ctx ):
   emb = discord.Embed ( title = 'Список команд')

   emb.add_field ( name = '{}clear'.format( PREFIX ), value = 'Очистка чата')
   emb.add_field ( name = '{}kick'.format( PREFIX ), value = 'Удаление учасника с сервера')
   emb.add_field ( name = '{}ban'.format( PREFIX ), value = 'Ограничение доступа к серверу')
   emb.add_field ( name = '{}unban'.format( PREFIX ), value = 'Удаление ограничения доступа к серверу')
   emb.add_field ( name = '{}mute'.format( PREFIX ), value = 'Ограничение доступа к чату')

   await ctx.send (embed = emb)

#MUTE
@client.command()  
@commands.has_permissions( administrator = True )
async def mute(ctx, member: discord.Member):
 	await ctx.channel.purge( limit = 1 )

 	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'MUTE') 

 	await member.add_roles( mute_role )
 	await ctx.send(f'У {member.mention}, ограничение чата за нарушения правил')


@client.command()  
@commands.has_permissions( administrator = True )
async def send_a(ctx):
	await ctx.channel.purge( limit = 1 )

	await ctx.author.send('там пост новый ес чо')

@client.command()
@commands.has_permissions( administrator = True )
async def send_all(ctx, member: discord.Member):
	await ctx.channel.purge( limit = 1 )

	await member.send(f'{member.name} глянь новый мост, от {ctx.author.name}')

token =('NjgxMDk4Nzg1NTA5ODY3NTQ1.XlJgtg.0GnFqlvl5eT-lGSrV31ne1JmIw0')

client.run ( token )
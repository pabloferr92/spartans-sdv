USE [sdv]
GO
/****** Object:  Table [dbo].[fechamento_banco]    Script Date: 22/04/2019 23:52:43 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[fechamento_banco](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_banco] [int] NULL,
	[volume_paginas] [nchar](10) NULL,
	[valor_paginas] [float] NULL,
	[qtde_releaser] [int] NULL,
	[valor_releaser] [float] NULL,
	[volume_policy] [int] NULL,
	[valor_policy] [float] NULL,
	[volume_charge_back] [int] NULL,
	[valor_charge_back] [float] NULL,
	[volume_tracking] [int] NULL,
	[valor_tracking] [float] NULL,
	[valor_total] [float] NULL,
	[mes_referencia] [date] NULL,
 CONSTRAINT [PK_fechamento_banco] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[fechamento_banco]  WITH CHECK ADD  CONSTRAINT [FK_fechamento_banco_banco_dados] FOREIGN KEY([id_banco])
REFERENCES [dbo].[banco_dados] ([id])
GO
ALTER TABLE [dbo].[fechamento_banco] CHECK CONSTRAINT [FK_fechamento_banco_banco_dados]
GO

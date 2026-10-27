CREATE TABLE [dbo].[Usuarios]
(
    [UsuarioId] INT IDENTITY(1,1) NOT NULL,
    [Nombre] NVARCHAR(100) NOT NULL,
    [Email] NVARCHAR(255) NOT NULL,
    [Telefono] VARCHAR(20) NULL,
    [Activo] BIT DEFAULT (1) NOT NULL,
    [FechaCreacion] DATETIME2(7) DEFAULT (SYSDATETIME()) NOT NULL,
    CONSTRAINT [PK_Usuarios] PRIMARY KEY CLUSTERED ([UsuarioId] ASC)
);

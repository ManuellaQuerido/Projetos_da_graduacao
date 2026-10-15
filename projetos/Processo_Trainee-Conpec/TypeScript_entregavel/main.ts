interface TransacaoAPI {
  Status: string;
  ID: number;
  Data: string;
  Nome: string;
  "Forma de Pagamento": string;
  Email: string;
  "Valor (R$)": string;
  "Cliente Novo": number;
}

function isTransacaoAPI(
  value: unknown,
): value is TransacaoAPI {
  if (typeof value !== "object" || value === null) {
    return false;
  }

  const obj = value as Record<string, unknown>;

  return (
    typeof obj.Status === "string" &&
    typeof obj.ID === "number" &&
    typeof obj.Data === "string" &&
    typeof obj.Nome === "string" &&
    typeof obj["Forma de Pagamento"] === "string" &&
    typeof obj.Email === "string" &&
    typeof obj["Valor (R$)"] === "string" &&
    typeof obj["Cliente Novo"] === "number"
  );
}

function converterValor(valor: string): number {
  if (valor === "-") {
    return 0;
  }

  return Number(
    valor.replace(/\./g, "").replace(",", "."),
  );
}

async function fetchData() {
  const response = await fetch(
    "https://api.origamid.dev/json/transacoes.json",
  );

  const data: unknown = await response.json();

  if (!Array.isArray(data)) {
    throw new Error("Formato inválido");
  }

  const transacoes = data.filter(isTransacaoAPI);

  // MOSTRA O FORMATO DA DATA NO CONSOLE
  console.log(transacoes[0].Data);

  const valorTotal = transacoes.reduce(
    (total, transacao) =>
      total + converterValor(transacao["Valor (R$)"]),
    0,
  );

  const credito = transacoes.filter(
    (t) =>
      t["Forma de Pagamento"] ===
      "Cartão de Crédito",
  ).length;

  const boleto = transacoes.filter(
    (t) => t["Forma de Pagamento"] === "Boleto",
  ).length;

  const paga = transacoes.filter(
    (t) => t.Status === "Paga",
  ).length;

  const recusada = transacoes.filter(
    (t) =>
      t.Status ===
      "Recusada pela operadora de cartão",
  ).length;

  const aguardando = transacoes.filter(
    (t) => t.Status === "Aguardando pagamento",
  ).length;

  const estornada = transacoes.filter(
    (t) => t.Status === "Estornada",
  ).length;

  const diasSemana = [
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
  ];

  const vendasPorDia: Record<string, number> = {};

transacoes.forEach((transacao) => {
  const [data] = transacao.Data.split(" ");

  const [dia, mes, ano] = data.split("/");

  const dataVenda = new Date(
    Number(ano),
    Number(mes) - 1,
    Number(dia),
  );

  const diaSemana =
    diasSemana[dataVenda.getDay()];

  vendasPorDia[diaSemana] =
    (vendasPorDia[diaSemana] ?? 0) + 1;
});

  const diaMaisVendas = Object.entries(
    vendasPorDia,
  ).sort((a, b) => b[1] - a[1])[0]?.[0];

  const estatisticas =
    document.getElementById("estatisticas");

  if (estatisticas) {
    estatisticas.innerHTML = `
      <p><strong>Total:</strong> ${valorTotal.toLocaleString(
        "pt-BR",
        {
          style: "currency",
          currency: "BRL",
        },
      )}</p>

      <p>Cartão de Crédito: ${credito}</p>
      <p>Boleto: ${boleto}</p>

      <p>Paga: ${paga}</p>
      <p>Recusada pela operadora de cartão: ${recusada}</p>
      <p>Aguardando pagamento: ${aguardando}</p>
      <p>Estornada: ${estornada}</p>

      <p>Dia com mais vendas: ${diaMaisVendas}</p>
    `;
  }

  const tbody =
    document.querySelector("tbody");

  if (tbody) {
    tbody.innerHTML = transacoes
      .map(
        (transacao) => `
        <tr>
          <td>${transacao.Nome}</td>
          <td>${transacao.Email}</td>
          <td>${transacao["Valor (R$)"]}</td>
          <td>${transacao["Forma de Pagamento"]}</td>
          <td>${transacao.Status}</td>
        </tr>
      `,
      )
      .join("");
  }
}

fetchData();
import { VersionedTransaction } from '@solana/web3.js';

export class Jupiter {
  constructor({ baseUrl, apiKey, slippageBps, priorityFeeMaxLamports }) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.apiKey = apiKey;
    this.slippageBps = slippageBps;
    this.priorityFeeMaxLamports = priorityFeeMaxLamports;
  }

  headers() {
    const h = { 'content-type': 'application/json' };
    if (this.apiKey) h['x-api-key'] = this.apiKey;
    return h;
  }

  // amount is a raw integer (lamports for SOL) as a string or bigint.
  async quote(inputMint, outputMint, amount) {
    const url = new URL(`${this.baseUrl}/quote`);
    url.searchParams.set('inputMint', inputMint);
    url.searchParams.set('outputMint', outputMint);
    url.searchParams.set('amount', amount.toString());
    url.searchParams.set('slippageBps', String(this.slippageBps));
    url.searchParams.set('restrictIntermediateTokens', 'true');
    const res = await fetch(url, { headers: this.headers() });
    const body = await res.json().catch(() => ({}));
    if (!res.ok || body.error || !body.outAmount) {
      throw new Error(`Jupiter quote failed (${res.status}): ${body.error || JSON.stringify(body).slice(0, 200)}`);
    }
    return body;
  }

  async buildSwap(quoteResponse, userPublicKey) {
    const res = await fetch(`${this.baseUrl}/swap`, {
      method: 'POST',
      headers: this.headers(),
      body: JSON.stringify({
        quoteResponse,
        userPublicKey,
        wrapAndUnwrapSol: true,
        dynamicComputeUnitLimit: true,
        dynamicSlippage: true,
        prioritizationFeeLamports: {
          priorityLevelWithMaxLamports: { maxLamports: this.priorityFeeMaxLamports, priorityLevel: 'veryHigh' },
        },
      }),
    });
    const body = await res.json().catch(() => ({}));
    if (!res.ok || !body.swapTransaction) {
      throw new Error(`Jupiter swap build failed (${res.status}): ${body.error || JSON.stringify(body).slice(0, 200)}`);
    }
    return VersionedTransaction.deserialize(Buffer.from(body.swapTransaction, 'base64'));
  }
}

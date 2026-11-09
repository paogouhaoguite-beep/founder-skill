import { Suspense } from "react";
import { notFound } from "next/navigation";
import ToolStudio from "@/components/ToolStudio";
import { getTool, TOOLS, type ToolId } from "@/lib/catalog";

export function generateStaticParams() {
  return TOOLS.map((t) => ({ tool: t.id }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ tool: string }> }) {
  const t = getTool((await params).tool);
  return { title: t ? `${t.name} · Flippers` : "Flippers" };
}

export default async function ToolPage({ params }: { params: Promise<{ tool: string }> }) {
  const { tool } = await params;
  if (!getTool(tool)) notFound();
  return (
    <Suspense>
      <ToolStudio key={tool} tool={tool as ToolId} />
    </Suspense>
  );
}
